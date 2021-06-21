import base64
from time import sleep
from aip import AipFace

import urllib.request
import cv2
import numpy
#import RPi.GPIO as GPIO
from PyQt5 import QtCore
import sys

import image_rc


from PyQt5.QtWidgets import (QWidget, QMessageBox, QLabel, QDialog,
  QApplication, QPushButton, QDesktopWidget, QLineEdit, QTabWidget)
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
##用户组信息
APP_ID = '16387188'
API_KEY = 'PlUcq4774qfYsAZRpmdlrpyi'
SECRET_KEY = 'pGQTUIgkvGXDWFBpYDKTwGolzGlBikqx'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
IMAGE_TYPE = 'BASE64'
groupid = 'XJS'
##这个groupid是对于人脸库来说的不同人有不同的组别
# GPIO.setwarnings(False)


# class Dialog(QDialog):
#     def __init__(self,parent = None):
#         QDialog.__init__(self,parent)

class GUI(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 160, 120, 100)
        self.tishi = QtWidgets.QPushButton(self)
        self.tishi.setText("关\n闭")
        self.tishi.setGeometry(QtCore.QRect(0, 0, 120, 100))


        self.tishi.setCheckable(False) # 设置默认
        self.tishi.toggle()  # 切换按钮状态




class GUI_2(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(240, 160, 100, 100)
        self.dhk = QtWidgets.QPushButton(self)
        self.dhk.setGeometry(QtCore.QRect(20, 220, 75, 23))
        self.dhk.setText("开门")#添加新人脸



        self.dhk_2 = QtWidgets.QPushButton(self)
        self.dhk_2.setGeometry(QtCore.QRect(290, 220, 75, 23))
        self.dhk_2.setText("添加新人脸")

        self.tishi.setCheckable(False) # 设置默认
        self.tishi.toggle()  # 切换按钮状态




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 320)
        Form.setStyleSheet("background-image: url(:/imgae/2.png);")




        self.fuwei = QtWidgets.QPushButton(Form)
        self.fuwei.setGeometry(QtCore.QRect(150, 40, 75, 23))
        self.fuwei.setObjectName("fuwei")
        self.fuwei.setStyleSheet("\n"
                                      "background-image: url(:/imgae/3_heroes_loadingscreen.png);")


        self.yunduan = QtWidgets.QPushButton(Form)
        self.yunduan.setGeometry(QtCore.QRect(20, 220, 75, 23))
        self.yunduan.setObjectName("yunduan")

        self.bendi = QtWidgets.QPushButton(Form)
        self.bendi.setGeometry(QtCore.QRect(150, 220, 75, 23))
        self.bendi.setObjectName("bendi")

        self.tuichu = QtWidgets.QPushButton(Form)
        self.tuichu.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.tuichu.setObjectName("tuichu")

        self.yunduan.setCheckable(False)  # 设置默认
        self.yunduan.toggle()  # 切换按钮状态
        self.yunduan.clicked.connect(self.cap)


        # self.fuwei.clicked.connect(lambda: self.wichBtn(self.fuwei))

        self.tuichu.setCheckable(False)  # 设置默认
        self.tuichu.toggle()  # 切换按钮状态



        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人脸识别"))
        self.fuwei.setText(_translate("Form", "锁门"))
        self.yunduan.setText(_translate("Form", "云端识别"))
        self.bendi.setText(_translate("Form", "人脸注册"))
        self.tuichu.setText(_translate("Form", "退出"))

    def cap(self,Form):

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        len_i = 0
        num = 0
        cv2.imshow('frame', frame)
        ex = GUI()
        ex.show()
        while (True):
            # 获取摄像头拍摄到的画面
            ret, frame = cap.read()
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)

            F = cv2.waitKey(1) & 0xFF
            cv2.namedWindow("frame", 0)
            cv2.resizeWindow("frame", 360, 320)
            cv2.imshow('frame', frame)


            if ex.tishi.isDown():
                cap.release()
                cv2.destroyAllWindows()
                break

            ##求矩阵的值不等于0
            if len(faces) > 0:
                cv2.imwrite("face.jpg", frame)



                # 最后，关闭所有窗口
                cap.release()
                cv2.destroyAllWindows()
                ex.close()
                f = open("face.jpg", 'rb')
                img = base64.b64encode(f.read())
                result = client.search(str(img, 'utf-8'), IMAGE_TYPE, groupid)
                a = result['result']['user_list'][0]['group_id']
                print(a)
                if (result['error_code'] == 0 & a=='XJS'):
                    ex_2 = GUI_2()
                    ex_2.show()
                    # print("successll")
                    # video.set_servoangle(self)
                break
            continue








class video(object):
    # 注意这个init 是否需要定义再说
    def __init__(self):
        self.servo = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo, GPIO.OUT)

    def set_servoangle(self):
        angle = 180
        pwm = GPIO.PWM(self.servo, 50)
        pwm.start(8)
        dc = angle / 18 + 3
        pwm.ChangeDutyCycle(dc)
        sleep(0.3)
        pwm.stop()

    def restart(self):
        angle = 0
        pwm = GPIO.PWM(self.servo, 50)
        pwm.start(8)
        dc = angle / 18 + 3
        pwm.ChangeDutyCycle(dc)
        sleep(0.3)
        pwm.stop()








if __name__ == '__main__':
    # GPIO.cleanup()
    # x = video()
    app = QtWidgets.QApplication(sys.argv)
    MinWindow = QtWidgets.QMainWindow()

    ui = Ui_Form()
    ui.setupUi(MinWindow)
    MinWindow.show()
    sys.exit(app.exec_())


