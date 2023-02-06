# !/usr/bin/python
#
from fabric.api import
from fabric.context_managers import *

from pprint import pprint

env.hosts = [
    '10.10.10.140', # 
    '10.10.10.193', #
]

env.user = "root"
env.password = "P@ssw0rd"

def get_system_health():
    discovery_commands = {
    "uptime": "uptime | awk '{print $3,$4}'",

    }
    health_commands = {
        "used_memory": "free"


    }
