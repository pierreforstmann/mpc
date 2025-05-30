#
# export_ffb
#
import os
import configparser

try:

    home = os.environ['HOME']
    installsdotini= home + "/" + ".mozilla/firefox/installs.ini"

    install_config = configparser.ConfigParser()
    install_config.read(installsdotini)
    sections =  install_config.sections()
    default_directory = install_config[sections[0]]['DEFAULT']

    sqlite_db_path = home  + "/.mozilla/firefox/" + default_directory + "/places.sqlite"
    sqlite_db_stat = os.stat(sqlite_db_path)
    print(sqlite_db_stat)

except:

    print ("Cannot find Mozilla data")
    exit(1)

