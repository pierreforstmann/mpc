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
import argparse

def update_item(p_item: int, p_price: float, p_brand: str):
    conn = psycopg2.connect("dbname=postgres user=test port=5442 password=test")
    cur = conn.cursor()
    try:
       cur.execute("""
                   SELECT item 
                   FROM public.items 
                   WHERE item = %s 
                   """, [p_item])
       ret = cur.fetchone();
       if (ret == None):
           print("Error: item ", p_item, " not found")
           return False

       cur.execute("""
                   UPDATE public.items 
                   SET price=%s, brand = %s
                   WHERE item = %s 
                   """, (p_price, p_brand, p_item))
       conn.commit()
       cur.close()
       conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Error in UPDATE", error)
        return False

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--item", required=True, help="""item number""")
    parser.add_argument("-p", "--price", required=True, help="""item price""")
    parser.add_argument("-b", "--brand", required=True, help="""brand name""")
    update_item(
            parser.parse_args().item,
            parser.parse_args().price,
            parser.parse_args().brand)

