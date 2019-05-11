#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5创建了一个简单的窗口。

作者: Jan Bodnar
网站: zetcode.com 
最后一次编辑: January 2015
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import untitled as wid

import sys

if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wid.Ui_MainWindow()
    # wid.Ui_MainWindow.PushButton.clicked.connect(MainWindow.close)

    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 
