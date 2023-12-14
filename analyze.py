#
# analyze.py
#
# Copyright Pierre Forstmann 2023
#
# ----------------------------------------------------------------------------------
import sys
import mailbox
import re

def get_mail_subjects(filename):
    mbox = mailbox.mbox(filename)
    regex = re.compile('[\s\S][#]\d+')
    for message in mbox:
       subject = message['subject']
       print("subject => ", subject, end='')
       if regex.search(subject):
           print(" bugno => ", regex.search(subject).group())
       else:
           print(" bugno => None", '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze.py mbox")
        sys.exit(1)

    get_mail_subjects(sys.argv[1])
