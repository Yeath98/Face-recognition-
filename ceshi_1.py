# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ceshi_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import  sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")



        self.pushButton.setCheckable(True)  # 设置已经被点击
        self.pushButton.toggle()  # 切换按钮状态
        self.pushButton.clicked.connect(self.btnState)
        self.pushButton.clicked.connect(lambda: self.wichBtn(self.pushButton))

        self.pushButton.setCheckable(True)#设置已经被点击
        self.pushButton.toggle()#切换按钮状态
        self.pushButton.clicked.connect(self.btnState)
        self.pushButton.clicked.connect(lambda :self.wichBtn(self.pushButton))







        self.openGLWidget = QtWidgets.QOpenGLWidget(Form)
        self.openGLWidget.setGeometry(QtCore.QRect(40, 70, 300, 200))
        self.openGLWidget.setObjectName("openGLWidget")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.openGLWidget.hide)



        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Window"))
        self.pushButton.setText(_translate("Form", "OK"))

    def btnState(self):
        if self.pushButton.isChecked():
            print("Btn_1被单击")
        else:
            print("Btn_1未被单击")
    def wichBtn(self,pushButton):
        print("点击的按钮是：" ,pushButton.text())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
