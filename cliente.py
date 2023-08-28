#!/usr/bin/env python
#_*_codings: utf8_*_

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('192.168.18.10', 7777))
cliente.close()