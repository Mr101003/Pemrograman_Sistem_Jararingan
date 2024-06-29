import paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
print("*** Connecting to server ***")
client.connect('192.168.200.63', username='psj', password='psj123')
stdin, stdout, stderr = client.exec_command('df -h /')
for line in stdout:
 print("result =>" + line.strip("\n"))
 
 client.close()
 
client2 = paramiko.SSHClient()
client2.load_system_host_keys()
client2.set_missing_host_key_policy(paramiko.WarningPolicy())
print("*** Connecting to server ***")
client2.connect('lp3.nurulfikri.ac.id', port=2299, username='psj', password='Psj-123')
stdin, stdout, stderr = client2.exec_command('/ip dhcp-server lease print')
for line in stdout:
 print("result => " + line.strip("\n"))