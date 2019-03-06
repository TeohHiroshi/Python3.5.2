#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 13:58
# @Author  : BokzBCheung
# @Site    : www.github.com/BokzBCheung
# @File    : basicTopics.py
# @Software: PyCharm
# @license : Copyright(C),BokzBCheung
# @Contact : BokzBCheung@gmail.com

# 顺序求和

# (1)函数版本
def summation_Tool(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum

# (2)基础版本
def summation_Basic(n):
    sum=0
    while n>0:
        sum+=n
        n-=1
    return sum

print(summation_Tool(100))
print(summation_Basic(100))

# 数组排序

# (1)函数版本
def sort_Tool(arrlist):
    arrlist.sort()
    return arrlist

# (2)冒泡版本
def sort_Bubble(arrlist):
    n=len(arrlist)
    for i in range(n-1):
        count=0
        for j in range(n-1-i):
            if arrlist[j]>arrlist[j+1]:
                arrlist[j],arrlist[j+1]=arrlist[j+1],arrlist[j]
                count+=1
        if count==0:
            break
    return arrlist

arrlist=[4,3,2,5,7,9,0]
print(sort_Tool(arrlist))
print(sort_Bubble(arrlist))

# 斐波那契数列
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(7))