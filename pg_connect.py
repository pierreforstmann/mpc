#
# pg_connect.py
#
# PG connection pool
#
# Copyright Pierre Forstmann 2023
#------------------------------------------------------------------------------------------------
import psycopg2
from psycopg2 import pool

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

connection = connection_pool.getconn()


