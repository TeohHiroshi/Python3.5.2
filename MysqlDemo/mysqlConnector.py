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
from mysql.connector import connection,errorcode

# #定义变量方式
# hostname='192.168.10.17'
# username='root'
# password='lf0507'
#
# # 定义连接信息
# conn = mysql.connector.connect(user=username,password=password,host=hostname,database='pythontest1')

#定义字典方式
config={
    'user':'root',
    'password':'lf0507',
    'host':'192.168.10.17',
    'database':'pythontest1'
}

try:
    conn = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("请检查用户名或密码！")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("请检查数据库名称！")
    else:
        print(err)

cursor = conn.cursor()

# 定义查询语句
query = "select user_name from t_userInfo"

cursor.execute(query)
names = cursor.fetchall()

for name in  names:
    print("{}".format(name))

cursor.close()
conn.close()

# 将list转化为string
# resuleStr = ''.join('%s' %pwd for pwd in values)

# print(cursor.rowcount)
# print(resuleStr)
