#
# pg_connect.py
#
# Python code to connect to  PG instance.
#
# $ python3 pg_connect.py
# 
# Copyright Pierre Forstmann 2023
#------------------------------------------------------------------------------------------------
import psycopg2
import os

conn = psycopg2.connect("dbname=postgres user=test port=5542 password=test")
cur = conn.cursor()
cur.execute("SELECT current_user")
print(cur.fetchone())
cur.close()
conn.close()
