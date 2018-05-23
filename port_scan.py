#!/usr/bin/python3
import socket
s = socket.socket()

# Exception handling for gai errors
try:
    s.connect(('ad.samsclass.info', 22))  # connect to server:22
    print(s.recv(1024))  # receives data up to 1024 chars from server
    s.close()
except socket.error as err:
    print(err)
