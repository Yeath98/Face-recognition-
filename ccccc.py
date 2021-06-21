# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'ccccc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
if __name__ == '__main__':
    # GPIO.cleanup()
    # x = video()
    app = QtWidgets.QApplication(sys.argv)
    MinWindow = QtWidgets.QMainWindow()

    ui = Ui_Form()
    ui.setupUi(MinWindow)
    MinWindow.show()
    sys.exit(app.exec_())

