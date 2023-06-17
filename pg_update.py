#
# pg_update.py
#
# Python code to update PG table
#
# $ python3 pg_update.py
# 
# Copyright Pierre Forstmann 2023
#------------------------------------------------------------------------------------------------
import psycopg2
import os

def update_item(p_item: int, p_price: float, p_brand: str):
    conn = psycopg2.connect("dbname=postgres user=test port=5442 password=test")
    cur = conn.cursor()
    cur.execute("""
                UPDATE public.items 
                SET price=%s, brand = %s
                WHERE item = %s 
                """, (p_price, p_brand, p_item))
    conn.commit()
    cur.close()
    conn.close()

p_item = 1
p_price = 3.0
p_brand = "C"

update_item(p_item, p_price, p_brand)

