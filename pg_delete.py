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
import argparse 
import pg_connect

def delete_item(p_item: int):
    conn = pg_connect.connection 
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
                   DELETE FROM public.items 
                   WHERE item = %s 
                   """, [p_item])
        conn.commit()
        cur.close()

    except (Exception, psycopg2.Error) as error:
        print("Error in DELETE", error)
        return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--item", required=True, help="""item number""")
    delete_item(parser.parse_args().item)

