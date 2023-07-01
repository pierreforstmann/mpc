#
# working.py -  Python Fast API Tutorial
#
# needs:
# pip install fastapi
# pip install uvicorn
# pip install loguru
#
#
# application server to be started in working.py directory with: 
# uvicorn working:app --reload
#
# -------------------------------------------------------------
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import psycopg2
from psycopg2 import pool
from loguru import logger
import configparser

class Item(BaseModel):
    item: int = 0
    price: float = 0
    brand: str = ""

app = FastAPI()

logger.add("/tmp/working.log", format="{time} {level} {message}", level="DEBUG")

config = configparser.ConfigParser()
config.read("working.ini")
pg_user = config['default']['user']
pg_password = config['default']['password']
pg_port = config['default']['port']
pg_host = config['default']['host']
pg_database = config['default']['database']


connection_pool = psycopg2.pool.SimpleConnectionPool(
                     1,     # minimum number of connections
                     1,     # maximum number of connections
                     user=pg_user,
                     password=pg_password,
                     host=pg_host,
                     port=pg_port,
                     database=pg_database
                   )

# Get a connection from the pool
connection = connection_pool.getconn()


# http://127.0.0.1:8000/
@app.get("/")
def home():
    logger.debug("Testing: OK")
    return {"Data": "Testing"}


# http://127.0.0.1:8000/about
@app.get("/about")
def about():
    logger.debug("About: OK")
    return {"Data": "About"}

# http://127.0.0.1:8000/get-item
@app.get("/get-item/")
def get_item() -> Item:
    local_item = Item()
    return local_item


# http://127.0.0.1:8000/get-item/1
@app.get("/get-item/{item_id}")
def get_item(p_item: int) -> Item:
    logger.debug("entry get_item")
    conn = connection 
    cur = conn.cursor()
    local_item = Item()
    logger.debug("try ... SELECT")
    try:
        cur.execute("""
                    SELECT item, price, brand
                    FROM public.items 
                    WHERE item = %s;
                    """, [p_item])
        row = (cur.fetchone())
        if row == None:
            local_item.item = -1
            local_item.brand = ""
            local_item.price = -1
        else:
            local_item.item = row[0]
            local_item.brand = row[2]
            local_item.price = row[1]
        logger.debug("end get_item")
        return local_item
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error in SELECT", error)
        
    cur.close()


#
@app.post("/create-item/{item_id}")
def create_item(item: Item):
    logger.debug("entry create_item")
    conn = connection 
    cur = conn.cursor()   
    try:
        cur.execute("""
                   INSERT INTO public.items (item, price, brand)
                   VALUES (%s, %s, %s);
                   """, (item.item, item.price, item.brand))
        conn.commit()
        cur.close()
        logger.debug("end create_item")
    except (Exception, psycopg2.Error) as error:
       print("Error in INSERT", error)
       conn.rollback()       

    return item


#
@app.delete("/delete-item/{item_id}")
def delete_item(p_item: int):
    local_item = Item()
    conn = connection
    cur = conn.cursor()
    try:
        cur.execute("""
                    SELECT item, brand, price
                    FROM public.items
                    WHERE item = %s
                    """, [p_item])
        row = cur.fetchone();
        if (row == None):
            local_item.item = -1
            local_item.brand = ""
            local_item.price = -1
            return local_item
        else:
            local_item.item = row[0]
            local_item.brand = row[1]
            local_item.price = row[2]

        cur.execute("""
                   DELETE FROM public.items 
                   WHERE item = %s 
                   """, [p_item])
        conn.commit()
        cur.close()

    except (Exception, psycopg2.Error) as error:
        print("Error in DELETE", error)
        conn.rollback()

    return local_item


#
@app.put("/update-item/{item_id}")
def update_item(p_item_id: int, p_item: Item):
    local_item = Item()
    conn = connection
    cur = conn.cursor()
    try:
        cur.execute("""
                    SELECT item, brand, price
                    FROM public.items
                    WHERE item = %s
                    """, [p_item_id])
        row = cur.fetchone();
        if (row == None):
            local_item.item = -1
            local_item.brand = ""
            local_item.price = -1
            return local_item
        else:
            # no PK change
            local_item.item = p_item_id
            local_item.brand = p_item.brand
            local_item.price = p_item.price

        cur.execute("""
                   UPDATE public.items 
                   SET price=%s, brand=%s
                   WHERE item = %s 
                   """, (local_item.price, local_item.brand, p_item_id))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.Error) as error:
        print("Error in UPDATE", error)
        conn.rollback()

    return local_item
