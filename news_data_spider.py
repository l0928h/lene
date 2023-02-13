#
from urllib.parse import urlparse
#
from pprint import pprint
import requests


def get_url():
    url = "https://fund.cnyes.com/search/?categoryAbbr=C74&classCurrency=TWD,USD&investmentArea=A13&page=2"
    uc = urlparse(url)
    print("NetLoc:", uc.netloc)
    print("Path:", uc.path)

    q_cmds = uc.query.split('&')
    print("Query Commands:")
    for cmd in q_cmds:
        print(cmd)

def get_data():
    url = 'https://news.pts.org.tw/list/0'
    html = requests.get(url).text.splitlines()
    for i in range(10):
        print(html[i])

def get_email():
    regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    url = 'http://xxxx.xxx.xxx'
    html = requests.get(url).text
    emails = re.findall(regex,html)
    for email in emails:
        print(email)
        

get_url()
get_data()

