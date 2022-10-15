#
# ora_connect_external.py
#
# Python code to connect to local Oracle database instance with externally identified user account.
#
# Tested with python 3.6 on Alma Linux 8.6 with Oracle XE 21C
#
# Setup with 'oracle' account:
# $ python3 -m pip install oracledb --user
#
# run in XE 21C connected with SYS:
# alter system set os_authent_prefix='' scope=spfile;
# alter system set common_user_prefix='' scope=spfile;
# startup force;
# create user oracle identified externally;
# grant dba to oracle;
# exit
# $ python3  ora_connect_external.py
# 
# Copyright Pierre Forstmann 2022
#------------------------------------------------------------------------------------------------
import oracledb
import os

oracledb.init_oracle_client(lib_dir=r"/opt/oracle/product/21c/dbhomeXE/lib")
with oracledb.connect() as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)
