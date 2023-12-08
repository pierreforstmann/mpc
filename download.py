#
# download.py
#
# Copyright Pierre Forstmann 2023
#
# ----------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse

url_auth = 'https://www.postgresql.org/account/login/?next=/account'

parsed_url = urlparse('https://www.postgresql.org/list/pgsql-bugs/');
root_url = parsed_url.hostname

html_text = requests.get('https://www.postgresql.org/list/pgsql-bugs/').text
soup = BeautifulSoup(html_text, 'lxml')
relative_tag_bugs_list = soup.find_all(name='a', string=(re.compile("mbox")))

relative_url_bugs_list = []
for tag in relative_tag_bugs_list:
    relative_url_bugs_list.append(str(tag))

absolute_url_bugs_list = []
for relative_url in relative_url_bugs_list:
    absolute_url_bugs_list.append('https://' + root_url + relative_url.split('"')[1])

print("Trying to authenticate ...")

# .pgopass syntax (NB: ending ':' is needed to avoid '\n' in password)
# <username>:<password>:
with open(".pgopass","r") as f:
          userpass = f.read()
          myusername = userpass.split(":")[0]
          mypassword = userpass.split(":")[1]

session = requests.session()
session.get(url_auth)
if 'csrftoken' in session.cookies:
    csrftoken = session.cookies['csrftoken']
else:
    print(" ... cannot find crsftoken. Exit.")
    exit()

login_data = dict(username =  myusername, password = mypassword, csrfmiddlewaretoken = csrftoken, this_is_the_login_form = "1", next = "")
response = session.post(url_auth, data = login_data, headers = dict(Referer = url_auth))
status = str(response.status_code)
print('status: ' + status)

if status == "200":
    print (" ... authentication succeeded.")
else:
    print (" ... authentication failed. Exit.")
    exit()

for url in absolute_url_bugs_list:
    print('Downloading ' + url + '... ')
    response = session.get(url)
    print('status: ' + str(response.status_code))
    if status == '200':
        print('... GET: OK' + ' ...')
    else:
        print('... GET: failed. Exit.')
        exit()
    mbox = url.split('/')[-1]
    with open(mbox, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=4096):
            fd.write(chunk)
    print(f'... Writing {mbox} to file system: done.')
