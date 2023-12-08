import requests
from urllib.parse import urlparse

url_auth = 'https://www.postgresql.org/account/login/?next=/account'
url_mbox = 'https://www.postgresql.org/list/pgsql-bugs/mbox/pgsql-bugs.202312'


with open(".pgopass","r") as f:
          userpass = f.read()
          myusername = userpass.split(":")[0]
          mypassword = userpass.split(":")[1]
print(myusername)
print(mypassword)

print("=> try authenticate ...")
session = requests.session()

session.get(url_auth)
if 'csrftoken' in session.cookies:
    csrftoken = session.cookies['csrftoken']
else:
    print(" ... cannot find crsftoken")
    exit()


login_data = dict(username =  myusername, password = mypassword, csrfmiddlewaretoken = csrftoken, this_is_the_login_form = "1", next = "")
print (login_data)
response = session.post(url_auth, data = login_data, headers = dict(Referer = url_auth))
status = str(response.status_code)
print('status: ' + status)
print(response.content)

if status == "200":
    print (" ... authentication succeeded.")
else:
    print (" ... authentication failed.")
    exit()

response = session.get(url_mbox)
print('status: ' + str(response.status_code))
print('... done')
