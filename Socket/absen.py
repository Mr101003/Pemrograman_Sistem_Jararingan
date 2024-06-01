# echo-client.py

import socket

HOST = "10.0.2.53"  # The server's hostname or IP address
PORT = 7777  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"0110222178,Mu'adz")
    data = s.recv(1024)

print(f"Received {data!r}")