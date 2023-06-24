#
# Python FAST API Tutorial
#
# needs:
# pip install fastpi
# pip install uvicorn
#
# working.py
#
# application server to be started in working.py directory with: 
# uvicorn working:app --reload
#
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import psycopg2
from psycopg2 import pool
from loguru import logger

app = FastAPI()

inventory = {
        }

connection_pool = psycopg2.pool.SimpleConnectionPool(
                     1,     # minimum number of connections
                     1,     # maximum number of connections
                     user="test",
                     password="test",
                     host="localhost",
                     port="5442",
                     database="postgres"
                   )

# Get a connection from the pool
logger.add("/tmp/working.log", format="{time} {level} {message}", level="DEBUG")
connection = connection_pool.getconn()


class Item(BaseModel):
    item: int = 0
    price: float = 0
    brand: str = ""

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

# http://127.0.0.1:8000/get-item 
@app.get("/get-item/{item_id}")
def get_item(p_item: int) -> Item:
    logger.debug("entry")
    conn = connection 
    cur = conn.cursor()
    local_item = Item()
    logger.debug("start")
    try:
        cur.execute("""
                    SELECT item, price, brand
                    FROM public.items 
                    WHERE item = %s;
                    """, [p_item])
        row = (cur.fetchone())
        local_item.item = row[0]
        local_item.brand = row[2]
        local_item.price = row[1]
        return local_item
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error in SELECT", error)
        
    cur.close()


# http://127.0.0.1:8000/get-by-name/1?test=2&name=Milk
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found")

#
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}

    inventory[item_id] = item 
    return inventory[item_id]
    
#

#
@app.delete("/delete-item/{item_id}")
def delete_item(item_id : int = Path( description = "The ID of the ititem you want to delete", gt=0)):
    if item_id not in inventory:
        return {"Error": "ID does not exist."}

    del inventory[item_id]

