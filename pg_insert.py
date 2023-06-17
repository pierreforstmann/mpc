#
# pg_insert.py
#
# Python code to insert into PG table
#
# $ python3 pg_insert.py
# 
# Copyright Pierre Forstmann 2023
#------------------------------------------------------------------------------------------------
import psycopg2
import os

def insert_item(p_item: int, p_price: float, p_brand: str):
    conn = psycopg2.connect("dbname=postgres user=test port=5442 password=test")
    cur = conn.cursor()
    try:
       cur.execute("""
                   INSERT INTO public.items (item, price, brand)
                   VALUES (%s, %s, %s);
                   """, (p_item, p_price, p_brand))
       conn.commit()
       cur.close()
       conn.close()

    except (Exception, psycopg2.Error) as error:
       print("Error in INSERT", error)
       return False

    return True

p_item = 1
p_price = 2.0
p_brand = "B"

insert_item(p_item, p_price, p_brand)

