#
# analyze.py
#
# Copyright Pierre Forstmann 2023
#
# ----------------------------------------------------------------------------------
import sys
import mailbox
import re
import sqlite3
from dateutil.parser import *
from dateutil import tz
import datetime

bugrefd = {}

def get_mail_data(filename):
    global bugrefd
    mbox = mailbox.mbox(filename)
    subject_regex = re.compile('BUG (#\d+)')
    for message in mbox:
       subject = message['subject']
       date = message['Date']
       if subject is not None and date is not None:
           if subject_regex.search(subject):
                bugref = subject_regex.search(subject).group(1)
                # print(" bugno => ", bugref)
                date_regex = re.compile('[A-Za-z]+[,]\s\d+\s[A-Za-z]+\s\d+\s\d+:\d+:\d+\s[+-]\d+')
                dateref  = date_regex.search(date).group()
                dt = parse(dateref)
                dt_str = dt.astimezone(tz.tzutc()).isoformat()
                if bugref not in bugrefd:
                    bugrefd[bugref] = ((1, dt_str, message['Message-Id']))
                else:
                    bugrefd[bugref] = ((bugrefd[bugref][0] + 1, dt_str, message['Message-Id']))
    print("current bugrefd => ", bugrefd)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python analyze.py from-year to-year")
        sys.exit(1)
    from_year = int(sys.argv[1])
    to_year = int(sys.argv[2])
    #
    for year in range (from_year, to_year + 1):
        for month_number in range(1,13):
            if month_number <= 9:
                month_string = "0" + str(month_number)
            else:
                month_string = str(month_number)
            mbox = "pgsql-bugs." + str(year) + month_string
            print("mbox =>", mbox)
            get_mail_data(mbox)
    #
    print("final bugrefd =>", bugrefd)
    #
    connexion = sqlite3.connect("bugs.db")
    cursor = connexion.cursor()
    for key, value in bugrefd.items():
        data = (key, value[0], value[1], value[2])
        cursor.execute("INSERT into bugs values(?, ?, ?, ?)", data)
    connexion.commit()