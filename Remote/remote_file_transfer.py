import paramiko
transport = paramiko.Transport(("192.168.200.63", 22))
transport.connect(None,"psj","psj123")
sftp = paramiko.SFTPClient.from_transport(transport)
# Download
filepath = "/home/psj/latihan/Mu'adz.txt"
localpath = "Mu'adz.txt"
sftp.put(localpath, filepath) #put untuk upload, get untuk download
sftp.close()
transport.close()