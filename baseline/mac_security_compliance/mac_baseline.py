import os, sys, subprocess, platform, re
import xml.etree.ElementTree as ET


def get_data():
    raw_data = []
    acc_data = []
    applications = []
    raw_data.append(subprocess.check_output(["whoami"]))
    raw_data.append(subprocess.check_output(["hostname"]))
    acc_data.append(subprocess.check_output(["defaults read MobileMeAccounts"], shell=True))
    applications.append(subprocess.check_output(["ls -l /Applications"], shell=True))

#    print(applications[1])


    with open('devicedata.log', 'w') as fp:        
        fp.write(str(raw_data))
    with open('applications.log', 'w') as fp:
        fp.write(str(applications))
    with open('accountdata.log', 'w') as fp:
        fp.write(str(acc_data))       
    print(raw_data)
    print(len(raw_data))
#    print(applications)

def data_parse():
    tree = ET.parse('MM-B-100563.local.spx')
    root = tree.getroot()
    for string in root.iter('string'):
        if string.text == 'SentinelOne':
            print('AntiVirus is SentinelOne')
        if string.text == 'spfirewall_globalstate_limit_connections':
            print('Firewall is on')
get_data()
data_parse()
