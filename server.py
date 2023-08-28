#!/usr/bin/env python
#_*_codings: utf8_*_

import socket

def upserver():
    global server
    global ip
    global target

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsocket(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(['192.168.18.10', 7777])
    server.listen(1)

    print('Servidor processando, esperando uma conexao...')

    target, ip = socket.accept()
    print(f'Conexao recebida {ip[0]}')

upserver()
server.close()