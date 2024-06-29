import paramiko

#Interkasi ke server linux
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
print("*** Connecting...to server")
client.connect('192.168.200.63', username='psj', password='psj123')
stdin, stdout, stderr = client.exec_command('df -h /') #Kirim perintah utk lihat disk usage
#Modif agar menampilkan output sbb:
# Penggunaan Disk saat ini mencapai : 27%
for line in stdout:
    if line.find("/") >= 0:
        #print("#result => " + line.strip("\n"))
        arr_line = line.split(" ")
        
        print(f"[server] Penggunaan Disk saat ini mencapai : {arr_line[-2]}")
        
client.close()


# Interkasi ke router mikrotik
client2 = paramiko.SSHClient()
client2.load_system_host_keys()
client2.set_missing_host_key_policy(paramiko.WarningPolicy())
print("*** Connecting...to Router")
client2.connect('lp3.nurulfikri.ac.id', port=2299,username='psj', password='Psj-123')
stdin, stdout, stderr = client2.exec_command('/ip dhcp-server lease print') #kirim perintah utk lihat daftar ip/klien tersambung
total = 0
for line in stdout:
    
    #print("#result => " + line.strip("\n"))
    if line.find("bound") >= 0 :
        total = total + 1