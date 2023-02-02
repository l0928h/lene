import os
def test_net():
    res = os.system('ping 8.8.8.8')
    if res: #
        Login()
    else: #
        print('ping ok')