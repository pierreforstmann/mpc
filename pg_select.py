#
# pg_select.py
#
# Python code to select data from PG table
#
# $ python3 pg_select.py
# 
# Copyright Pierre Forstmann 2023
#------------------------------------------------------------------------------------------------
import psycopg2
from psycopg2 import connect
import argparse

import os

def select_item(p_item: int) -> bool:
    conn = psycopg2.connect("dbname=postgres user=test port=5442 password=test")
    cur = conn.cursor()
    try:
        cur.execute("""
                    SELECT item, price, brand
                    FROM public.items 
                    WHERE item = %s;
                    """, [p_item])
        result = (cur.fetchall())
        for row in result:
            print("item = ", row[0],)
            print("brand = ", row[2])
            print("price = ", row[1], "\n");
        conn.commit()

    except (Exception, pgsycopg2.Error) as error:
        print("Error in SELECT", error)
        return False

    cur.close()
    conn.close()
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--item", required=True, help="""item number""")
    print(select_item(parser.parse_args().item))

