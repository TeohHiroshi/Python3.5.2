#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-15 15:40
# @Author  : BokzBCheung
# @Site    : www.github.com/BokzBCheung
# @File    : main.py
# @Software: PyCharm
# @license : Copyright(C),BokzBCheung
# @Contact : BokzBCheung@gmail.com

import sys
from GUIDemo import guiPyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = guiPyqt5.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
