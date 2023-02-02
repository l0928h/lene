from subprocess import run
def test_net():
    #
    #
    res = run('ping 8.8.8.8',shell=True)
    if res.returncode:
        Login()
    else:
        print('ping ok')
