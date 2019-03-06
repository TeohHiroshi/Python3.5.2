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

# 二分法查找

# 递归方法
def search_binary_recursion(lst,value,low,high):
    if high<low:
        return None
    else:
        mid=int((low+high)/2)
        if lst[mid]<value:
            return search_binary_recursion(lst,value,mid+1,high)
        elif lst[mid]>value:
            return search_binary_recursion(lst,value,low,mid-1)
        else:
            return mid

# 循环方法
def search_binary_loop(lst,value):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=int((low+high)/2)
        if lst[mid]<value:
            low=mid+1
        elif lst[mid]>value:
            high=mid-1
        else:
            return mid

# 随机数组生成
import random
lst=[random.randint(1,100000) for _ in range(100000)]
lst.sort()
value=9999

print(search_binary_loop(lst,value))
print(search_binary_recursion(lst,value,0,len(lst)-1))

#性能测试
if __name__ == "__main__":
    import timeit
    def test_recursion():
        search_binary_recursion(lst, value, 0, len(lst) - 1)
    def test_loop():
        search_binary_loop(lst, value)
    t1=timeit.Timer("test_recursion",setup="from __main__ import test_recursion")
    t2=timeit.Timer("test_loop",setup="from __main__ import test_loop")
    print("Recursion:",t1.timeit())
    print("Loop:",t2.timeit())

