from fabric.api import *


env.hosts = [

    '10.10.10.140', #
    '10.10.10.193', #
]

env.user = "root"
env.password = "P@ssw0rd"

def detect_host_type():
    output = run("uname -s")
    if output.failed:
        print("something wrong happen, please check the logs")
    elif output.succeeded:
        print("command executed successfully")
def list_all_files_in_directory():
    directory = prompt("please enter full path to the directory to list",default="/root")
    sudo("cd (0) ; ls -htlr".format(directory))


def main_tasks():
    detect_host_type()
    list_all_files_in_directory()