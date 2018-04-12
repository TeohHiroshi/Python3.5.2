#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-04-12 16:45
# @Author  : BokzBCheung
# @Site    : 
# @File    : mysqlConnector.py
# @Software: PyCharm
# @license : Copyright(C),BokzBCheung
# @Contact : BokzBCheung@gmail.com
# 导入mysql驱动
import mysql.connector
import string
# 定义连接信息
conn = mysql.connector.connect(user='root',password='lf0507',database='mysql')
cursor = conn.cursor()

# 定义查询语句
sqlStr = "select Password from user where User='root'"
cursor.execute(sqlStr)

values = cursor.fetchall()

print(values)
# 将list转化为string
resuleStr = ','.join('%s' %pwd for pwd in values)

print(len(values))
# print(cursor.rowcount)
print(resuleStr)