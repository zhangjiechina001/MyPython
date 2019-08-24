import sys
from PyQt5 import QtWidgets,QtCore

app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QWidget()
widget.resize(400,400)
widget.setWindowTitle("first app")
widget.show()
# sys.exit(app.exec_())
import PyQt5
print(dir(PyQt5))