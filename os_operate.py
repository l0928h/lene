import subprocess
print(subprocess.Popen("ifconfig"))

print(subprocess.Popen(["cat", "interfaces"], cwd="/etc/network"))