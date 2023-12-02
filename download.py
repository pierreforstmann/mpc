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

for url in absolute_url_bugs_list:
    print(f"{url}")
