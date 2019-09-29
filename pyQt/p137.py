import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QApplication
from PyQt5.QtGui import QFont, QIcon


class Winform(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif',10))
        self.setToolTip('这是一个')
        self.setGeometry(200,300,400,400)
        self.setWindowTitle('气泡提示demo')
        self.setWindowIcon(QIcon('D:\\360安全浏览器下载\\48V_OCV_Test\\48V_OCV_Test\\48V_OCV_Test\\Logos\\CATL.ico'))

if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Winform()
    win.show()
    sys.exit(app.exec_())