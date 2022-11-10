from netmiko.ssh_dispatcher import ConnectHandler
data = {'device_type':'huawei', 
        'ip':'192.168.0.1',
        'username':'satyam',
        'password': 'satya@123'}
net_connect = ConnectHandler(**data)
show = net_connect.send_command('dis ip int des')
print(show)
net_connect.disconnect()
file = open('data.txt','a')
file.write(show)
file.write('-'*20)