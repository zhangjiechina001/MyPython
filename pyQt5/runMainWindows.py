from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import mainwindowsHlayout

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainwindow=QMainWindow()
    ui=mainwindowsHlayout.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
