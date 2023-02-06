from netmiko import ConnectHandler

SW2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.88.112',
    'username': 'admin',
    'password': 'P@ssw0rd',
    'secret': 'P@ssw0rd',
}

core_sw_config = ["int range gig0/1 - 2","switchport trunk encapsulation dotlq",
                  "switchport mode trunk",
                  "switchport trunk allowed vlan 1,2"]

print "##### Connecting to Device {0} #####".format(SW2['ip'])
net_connect = ConnectHandler(**SW2)
net_connect.enable()
print "***** Sending Configuration to Device *****"
net_connect.send_config_set(core_sw_config)
