from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys

class windows(QWidget):
    def __init__(self):
        super().__init__()

        lable1=QLabel(self)
        lable2 = QLabel(self)
        lable3 = QLabel(self)
        lable4= QLabel(self)

        #1.初始化标签控件
        lable1.setText('这是一个文本标签。')
        lable1.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        lable1.setPalette(palette)
        lable1.setAlignment(Qt.AlignCenter)

        lable2.setText("<a href='#'>欢迎使用Python GUI应用</a>")
        lable3.setAlignment(Qt.AlignCenter)
        lable3.setToolTip('这是一个图片标签')
        lable3.setPixmap(QPixmap('D:\\manowar01.jpg'))

        lable4.setText("<a herf='http://www.baidu.com'>欢迎访问百度</a>")
        lable4.setAlignment(Qt.AlignRight)
        lable4.setToolTip('这是一个超链接的标签')

        #2.在窗口布局中添加控件
        vbox=QVBoxLayout()
        vbox.addWidget(lable1)
        vbox.addStretch()
        vbox.addWidget(lable2)
        vbox.addStretch()
        vbox.addWidget(lable3)
        vbox.addStretch()
        vbox.addWidget(lable4)
        vbox.addStretch()

        #3.允许label1控件访问超链接
        lable1.setOpenExternalLinks(True)

        lable4.setOpenExternalLinks(True)

        lable4.linkActivated.connect(self.link_clicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel例子')


    def link_hovered(self):
        print('当鼠标滑过label-2标签时，触发事件')
    def link_clicked(self):
        print('当用鼠标点击label-4标签时，触发事件')

if __name__=='__main__':
    app=QApplication(sys.argv)
    win=windows()
    win.show()
    sys.exit(app.exec_())