import paramiko
f = 'test.docx'
transport = paramiko.Transport(("192.168.10.1", 22))
transport.connect(None,'namauser','passworduser')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get(f,"/tmp/data.docx")
sftp.close()