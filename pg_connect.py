#
# pg_connect.py
#
# PG connection pool
#
# Copyright Pierre Forstmann 2023
#------------------------------------------------------------------------------
import configparser
import psycopg2
from psycopg2 import pool

config = configparser.ConfigParser()
config.read("pg_connect.ini")
pg_user = config['default']['user']
pg_password = config['default']['password']
pg_port = config['default']['port']
pg_host = config['default']['host']
pg_database = config['default']['database']

connection_pool = psycopg2.pool.SimpleConnectionPool(
                     1,     # minimum number of connections
                     1,     # maximum number of connections
                     user=pg_user,
                     password=pg_password,
                     host=pg_host,
                     port=pg_port,
                     database=pg_database
                   )

# Get a connection from the pool

connection = connection_pool.getconn()


