#!/usr/bin/python3
import socket
for port in range(9999):
    s = socket.socket()
    s.settimeout(2)
    #port = int(input('Port: '))  # manual input for specific port

    # Exception handling for gai errors
    try:
        s.connect(('ad.samsclass.info', port))  # connect to server:22
        banner = s.recv(1024)
        print(f'Port #{port}: {banner}')  # receives data up to 1024 chars from server
        s.close()
        if 'congratulations' in banner.decode('utf8').lower():
            break
    except socket.error as err:
        print(f'Port #{port}: {err}')
