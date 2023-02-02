import contextlib
import os
import queue
import requests
import sys
import threading
import time

FILTERED = [".jpg", ".gif", ".png", ".css"]
TARGET = "http://"



def test_remote():
    while not web_paths.get()
    path = web_paths.get()
    url = f'{target}{path}'
    time.sleep(2)  #
    r = requests.get(url)
    if r.status_code == 200:
        answers.put(url)
        sys.stdout.write('+')
    else:
        sys.stdout.write('x')
    sys.stdout.flush()


def run():
    myhreads = list()
    for i in range(THREADS):
        print(f'Spawning thread {i}')
        t = threading.Thread(target=test_remote)
        mythreads.append(t)
        t.start()

for thread in mythreads:
    thread.join()

if __name__ == '__main__':
    with chdir("/home/black/Downloads/wordpress"):
        gather_paths()
    input('Press return to continue.')

    run()
    with open('myanswers.txt','w') as f:
        while not answers.empty():
            f.write(f'{answers.get()}\n')
    print('done')


