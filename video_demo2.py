import base64
from time import sleep
from aip import AipFace
import urllib.request
import cv2
import numpy
import RPi.GPIO as GPIO
##用户组信息
APP_ID = '16387188'
API_KEY = 'PlUcq4774qfYsAZRpmdlrpyi'
SECRET_KEY = 'pGQTUIgkvGXDWFBpYDKTwGolzGlBikqx'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
IMAGE_TYPE='BASE64'
groupid='XJS'
##这个groupid是对于人脸库来说的不同人有不同的组别
GPIO.setwarnings(False)

class video(object):
    #注意这个init 是否需要定义再说
    def __init__(self):
        self.servo = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo, GPIO.OUT)

    def set_servoangle(self):
        angle = 180
        pwm = GPIO.PWM(self.servo,50)
        pwm.start(8)
        dc = angle/18+3
        pwm.ChangeDutyCycle(dc)
        sleep(0.3)
        pwm.stop()

    def restart():
        angle = 0
        pwm = GPIO.PWM(self.servo, 50)
        pwm.start(8)
        dc = angle / 18 + 3
        pwm.ChangeDutyCycle(dc)
        sleep(0.3)
        pwm.stop()

    def cap(self):
        
        print('1')
        
        face_cascade = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)        
        len_i = 0
        num = 0
        while (True):
            # 获取摄像头拍摄到的画面
            ret, frame = cap.read()
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            F = cv2.waitKey(1) & 0xFF
            cv2.namedWindow("frame", 0)
            cv2.resizeWindow("frame", 480, 320) 
            cv2.imshow('frame', frame)
            ##求矩阵的值不等于0
            if len(faces) > 0:
                cv2.imwrite("face.jpg", frame)
                # 最后，关闭所有窗口
                cap.release()
                cv2.destroyAllWindows()
                f = open("face.jpg", 'rb')
                img = base64.b64encode(f.read())
                result = client.search(str(img, 'utf-8'), IMAGE_TYPE, groupid)
                print(result)
                break
            continue
        if (result['error_code'] == 0):
           print("sucdessll")
           # video.set_servoangle(self)
    def a(self):
        print('aaaaaaa')

if __name__ =='__main__':
    GPIO.cleanup()
    x = video()
    x.cap()

