from netmiko import ConnectHandler
with open('ip.txt') as a:
    for b in a:
        router = {'device_type':'huawei',
                  'ip':b,
                  'username':'satyam',
                  'password':'satya@123'}
        print(b)
        conn = ConnectHandler(**router)
        print('connecting to > '+ b)
        print('-'*20)
        comm = conn.send_command('dis esn')
        print(comm)
        print()
        print('-'*40)
conn.disconnect()
time.sleep(10)
