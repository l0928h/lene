# -*- coding: utf-8 -*-
#

from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv) < 2:
    print("用法 <<target eurl>>")
    exit(1)

url= sys.argv[1]

html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
all_links = sp.find_all('a')

for link in all_links:
    href = link.get('href')
    if href != None and href.startswith('http://'):
        print(href)
