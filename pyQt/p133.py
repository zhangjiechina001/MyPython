# -*- coding:utf-8 -*-
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget

def firstQt():
    app=QApplication(sys.argv)
    window=QWidget()
    window.resize(300,200)
    window.move(200,200)
    window.setWindowTitle('第一个QT窗口')
    window.show()
    sys.exit(app.exec_())

class Icon(QWidget):
    def __init__(self,parent=None):
        super(Icon,self).__init__(parent=parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('程序图标')
        self.setWindowIcon(QIcon('D:\\360安全浏览器下载\\48V_OCV_Test\\48V_OCV_Test\\48V_OCV_Test\\Logos\\CATL.ico'))

def seconde():
    app=QApplication(sys.argv)
    icon=Icon()
    icon.show()
    sys.exit(app.exec_())
seconde()