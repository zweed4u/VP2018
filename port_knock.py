#!/usr/bin/python3
import time
import socket

init_knock_port = 3100
secret_hidden_knock_ports = [port for port in range(3100,4000,100)]  #non-inclusive (3100-3900)
hidden_service_port = 3003

for port in secret_hidden_knock_ports:
    # Exception handling for gai errors
    try:
        s = socket.socket()
        s.settimeout(2)

        s.connect(('ad.samsclass.info', init_knock_port))  # connect to server:3100
        banner = s.recv(1024)  # receives data up to 1024 chars from server
        print(f'Init Knock Port #{init_knock_port}: {banner}')
        #s.close()

        print('Knock on secret hidden port')
        s2 = socket.socket()
        s2.settimeout(2)
        s2.connect(('ad.samsclass.info', port))
        banner = s2.recv(1024)  # receives data up to 1024 chars from server
        print(f'Secret Hidden Port #{port}: {banner}')
        #s.close()

        print('See if port knock worked')
        s3 = socket.socket()
        s3.settimeout(2)
        s3.connect(('ad.samsclass.info', hidden_service_port))  # connect to server:22
        banner = s3.recv(1024)  # receives data up to 1024 chars from server
        print(f'Hidden Service Port #{hidden_service_port}: {banner}')
        s.close()
        s2.close()
        s3.close()
    except socket.error as err:
        print(f'Using Secret Hidden Port Knock on #{port}: {err}')
        try:
            s.close()
        except:
            pass
        try:
            s2.close()
        except:
            pass
        try:
            s3.close()
        except:
            pass

    print()
    time.sleep(2)