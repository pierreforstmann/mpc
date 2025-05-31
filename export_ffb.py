#
# export_ffb.py
#
# Export Firefox bookmarks on Linux
#
import os
import configparser
import sqlite3
import sys
import traceback

try:

    home = os.environ['HOME']
    installsdotini= home + "/" + ".mozilla/firefox/installs.ini"

    install_config = configparser.ConfigParser()
    install_config.read(installsdotini)
    sections =  install_config.sections()
    default_directory = install_config[sections[0]]['DEFAULT']
    print(f"default_directory: {default_directory}")

    sqlite_db_path = home  + "/.mozilla/firefox/" + default_directory + "/places.sqlite"
    print(f"sqlite_dbpath: {sqlite_db_path}")

    sqlite_db_stat = os.stat(sqlite_db_path)
    print(f"sqlite_db_stat: ${sqlite_db_stat}")
    
    url_count = 0
    connexion = sqlite3.connect(sqlite_db_path)
    cursor = connexion.cursor()
    cursor.execute("select url, description, title from moz_places;")
    result = cursor.fetchall()
    for url, title, description in result:
        print(f"url: {url}, title: {title}, description: {description}")
        url_count += 1
    print(f"{url_count} URL retrieved.")

except Exception as err:
    print("ERROR:")
    traceback.print_exc(file=sys.stdout)
    exit(1)

