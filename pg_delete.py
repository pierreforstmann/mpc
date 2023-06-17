#
# pg_delete.py
#
# Python code to delete PG table
#
# $ python3 pg_delete.py
# 
# Copyright Pierre Forstmann 2023
#------------------------------------------------------------------------------------------------
import psycopg2
import os

def delete_item(p_item: int):
    conn = psycopg2.connect("dbname=postgres user=test port=5442 password=test")
    cur = conn.cursor()
    cur.execute("""
                DELETE FROM public.items 
                WHERE item = %s 
                """, [p_item])
    conn.commit()
    cur.close()
    conn.close()

p_item = 1

delete_item(p_item)

