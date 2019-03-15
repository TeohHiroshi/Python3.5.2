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

def getUserName(currentName,currnetPwd):
    # #定义变量方式
    # hostname='192.168.10.17'
    # username='root'
    # password='lf0507'
    #
    # # 定义连接信息
    # conn = mysql.connector.connect(user=username,password=password,host=hostname,database='pythontest1')

    # 定义字典方式
    config = {
        'user': 'root',
        'password': 'lf0507',
        'host': '192.168.10.17',
        'database': 'pythontest1'
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
    query = "select username,password from t_userInfo"

    cursor.execute(query)
    names = cursor.fetchall()

    print(names)

    for name in names:
        print(name)
        if currentName in name:
            print(currentName,"属于当前检测用户，开始检测密码！")

            return 1
            break
        else:
            print(currentName,"不属于当前检索用户，即将进行下一轮检索！")
        # print("{}".format(name))



    # if currentName in names:
    #     print("true")
    #     return True;
    # else:
    #     print("fail")
    #     return False;

    cursor.close()
    conn.close()


    # 将list转化为string
    # resuleStr = ''.join('%s' %pwd for pwd in values)

    # print(cursor.rowcount)
    # print(resuleStr)

# 简单测试
# currentName = "bokzbcheung"
# if getUserName(currentName) == 1:
#     print("用户信息获取到,当前用户为：",currentName)
# else:
#     print("获取用户信息失败，请检查是否存在该用户！")