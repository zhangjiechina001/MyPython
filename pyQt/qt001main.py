from PyQt5.QtGui import QIcon

from QT001 import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

from pyQt.QT001 import Ui_Form


class MyClassWindow(QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(MyClassWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('程序图标')
        self.pushButton.clicked.connect(self.onButtonClick)
        self.setWindowIcon(QIcon('D:\\360安全浏览器下载\\48V_OCV_Test\\48V_OCV_Test\\48V_OCV_Test\\Logos\\CATL.ico'))
    def onButtonClick(self):
        sender=self.sender()
        print('这个窗体关闭了')
        self.close()

if __name__=='__main__':
    app=QApplication(sys.argv)
    myWin=MyClassWindow()
    myWin.show()
    sys.exit(app.exec_())