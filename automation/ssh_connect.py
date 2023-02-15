# !/usr/bin/python
#


import automation.ssh_connect as ssh_connect
import time

Channel = ssh_connect.SSHClient()
Channel.set_missing_host_key_policy(ssh_connect.AutoAddPolicy())
Channel.connect(hostname="10.10.88.112", username='admin', password='P@ssw0rd', look_for_keys=False,allow_agent=False)

shell = Channel.invoke_shell()

#
shell.send("enable\n")
shell.send("P@ssw0rd\n")
shell.send("terminal length 0\n")
shell.send("show ip int b\n")
shell.send("show arp \n")
time.sleep(2)
print shell.recv(5000)
Channel.close()
