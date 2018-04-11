#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-04-11 17:12
# @Author  : BokzBCheung
# @Site    : 
# @File    : tcpClient.py
# @Software: PyCharm
# @license : Copyright(C),BokzBCheung
# @Contact : BokzBCheung@gmail.com

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    #print(data)
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

while True:
    name_enter = input('Please enter your name:')
    #print(name_enter)
    name=bytes(name_enter,encoding='utf8')
    #print(name)
    if name_enter=='quit':
        break
    s.send(name)
    print(s.recv(1024).decode('utf-8'))

#s.send(b'exit')

s.close()