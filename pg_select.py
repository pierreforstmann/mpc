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
import pg_connect

def select_item(p_item: int) -> bool:
    conn = pg_connect.connection 
    cur = conn.cursor()
    try:
        cur.execute("""
                    SELECT item, price, brand
                    FROM public.items 
                    WHERE item = %s;
                    """, p_item)
        row = (cur.fetchone())
        print("item = ", row[0],)
        print("brand = ", row[2])
        print("price = ", row[1], "\n");
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error in SELECT", error)
        return False

    cur.close()
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--item", required=True, help="""item number""")
    print(select_item(parser.parse_args().item))

