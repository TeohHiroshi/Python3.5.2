#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-04-12 09:11
# @Author  : BokzBCheung
# @Site    : www.github.com/BokzBCheung
# @File    : guiTkinter.py
# @Software: PyCharm
# @license : Copyright(C),BokzBCheung
# @Contact : BokzBCheung@gmail.com

# 导入gui程序包
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 添加标题
        #self.helloLabel = Label(self,text='Hello world!')
        #self.helloLabel.pack()

        # 添加输入框
        self.nameInput = Entry(self)
        self.nameInput.pack()

        # 添加确认按钮
        self.confirmButton = Button(self,text='Confirm',command=self.confirm)
        self.confirmButton.pack()

        # 添加退出按钮
        #self.quitButton = Button(self,text='Quit',command=self.quit)
        #self.quitButton.pack()

    def confirm(self):
        name = self.nameInput.get()
        messagebox.showinfo(title='Hello~',message='Hello '+name+'!')


# 实例化派生类Application
app = Application()

# 设置窗口标题
app.master.title('Hello world')

# 设置窗口大小
app.master.geometry('400x200')

# 设置窗体是否可以拉伸
app.master.resizable(width=True,height=True)

# 主消息循环
app.mainloop()