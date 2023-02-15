import os
import platform
import subprocess


def get_system_os():
    sys = platform.system()
    print(sys)

def command():
    print(subprocess.Popen("ifconfig"))
    print(subprocess.Popen(["cat", "interfaces"], cwd="/etc/network"))

get_system_os()
print(get_system_os)