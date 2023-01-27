# -*- coding: utf-8-*-
#

from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urlparse

if len(sys.argv) < 2:
    print("用法: <target url>")
    exit(1)

url = sys.argv[1]
domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
all_links = sp.find_all(['a','img'])