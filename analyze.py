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
    mbox = mailbox.mbox(filename)
    regex = re.compile('[\s\S][#]\d+')
    for message in mbox:
       subject = message['subject']
       # print("subject => ", subject, end='')
       if regex.search(subject):
           bugref = regex.search(subject).group()
           # print(" bugno => ", bugref)
           if bugref not in bugrefd:
                bugrefd[bugref] = 1
           else:
               bugrefd[bugref] += 1
               
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze.py mbox")
        sys.exit(1)

    get_mail_subjects(sys.argv[1])
    print(bugrefd)
