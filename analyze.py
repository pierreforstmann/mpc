#
# analyze.py
#
# Copyright Pierre Forstmann 2023
#
# ----------------------------------------------------------------------------------
import sys
import mailbox
import re

bugrefd = {}

def get_mail_subjects(filename):
    global bugrefd
    mbox = mailbox.mbox(filename)
    regex = re.compile('[\s\S][#]\d+')
    for message in mbox:
       subject = message['subject']
       if subject is not None:
           if regex.search(subject):
                bugref = regex.search(subject).group()
                # print(" bugno => ", bugref)
                if bugref not in bugrefd:
                    bugrefd[bugref] = 1
                else:
                    bugrefd[bugref] += 1
    print("current bugrefd => ", bugrefd)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze.py year")
        sys.exit(1)
    for month_number in range(1,13):
        if month_number <= 9:
            month_string = "0" + str(month_number)
        else:
            month_string = str(month_number)
        mbox = "pgsql-bugs." + sys.argv[1] + month_string
        print("mbox =>", mbox)
        get_mail_subjects(mbox)
    print("final bugrefd =>", bugrefd)
