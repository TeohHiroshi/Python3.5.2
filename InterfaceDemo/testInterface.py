#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-06 14:24
# @Author  : BokzBCheung
# @Site    : www.github.com/bokzbcheung
# @File    : testInterface.py
# @Software: PyCharm
# @license : Copyright(C),BokzBCheung
# @Contact : BokzBCheung@gmail.com

from flask import Flask, request,json,jsonify
succJson = {"test": "成功！"}
failJson = {"test": "失败！"}

app = Flask(__name__)

@app.route('/testInterface',methods=['POST'])
def api():
    if request.method == "POST":

        data = request.get_data()
        data = json.loads(data)

        print("接受到数据为：",data)

        if data["data"] == "测试数据":

            print("返回数据为：",succJson)
            return jsonify(succJson)

        else:

            print("返回数据为：",failJson)
            return jsonify(failJson)

if __name__ == '__main__':
#    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1',port='8080')