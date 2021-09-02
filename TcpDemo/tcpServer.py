#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-04-11 17:11
# @Author  : BokzBCheung
# @Site    : 
# @File    : tcpServer.py
# @Software: PyCharm
# @license : Copyright(C),BokzBCheung
# @Contact : BokzBCheung@gmail.com
#引入socket
import socket
import threading
import time

#定义socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定端口
s.bind(('127.0.0.1',8888))

#开始监听
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            sock.send(b'you enter an EXIT command')
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

#等待连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

