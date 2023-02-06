import subprocess
p = subprocess.Popen("ping", "8.8.8.8", "-c", "3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
print("""==========The Standard Output is========== {}""".format(stdout))

print("""==========The Standard Error is========== {}""".format(stderr))