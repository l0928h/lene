import os,sys,subprocess
from pprint import pprint

# uname = platform.uname()
hostname = subprocess.check_output(["hostname"])
whoami = subprocess.check_output(["whoami"])
raw_data = []
# raw_data.append(uname)

raw_data.append(hostname)
raw_data.append(whoami)
with open('device_data.log', 'w') as fp:    
        fp.write(str(raw_data))

print(raw_data)