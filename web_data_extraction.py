import json
import requests
import hashlib
import datetime
import os.path
import _mysql


r = requests.get('http;//')
sig = hashlib.md5(r.text.encode('utf-8')).hexdigets()

if os.path.exists('eq_sig.txt'):
    with open('eq_sig.txt', 'r') as fp:
        old_sig = fp.read()
    with open('eq_sig.txt', 'w') as fp:
        fp.write(sig)
else:
    with open('eq_sig.txt', 'w') as fp:
        fp.write(sig)

if sig == old_sig:
    print('資料未更新，不需要處理...')
    exit()