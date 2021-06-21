# -*- coding: utf-8 -*-
import os
import sys
import socket
import json
import time
import random
from threading import Thread


from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.Temperature import Ui_Form
from utils.algorithmThread import TemperatureThread


class Temper(QMainWindow, Ui_Form):
    """
    温度模块
    """
    def __init__(self):
        super(Temper, self).__init__()
        self.setupUi(self)
        self.label_temp.setText("当前温度：00℃")
        self.label_result.hide()
        self.tem_val = 0
        # 线程 体温获取线程
        self.temthread = TemperatureThread(self)
        self.temthread.tem_signal.connect(self.set_temp)
        self.temthread.start()

    def set_temp(self):
        """
        温度显示
        :return:
        """
        if self.tem_val:
            self.label_temp.setText('当前温度：{:.1f}℃'.format(self.tem_val))
            if self.tem_val >= 37.3:
                self.label_result.show()
            else:
                self.label_result.hide()
        else:
            self.label_result.hide()
            self.label_temp.setText("当前温度：00℃")
    #==========================================================
    def socket_client(host, port):
        ''''
        创建TCP连接
        '''
        handshare_data = {
            "t": 1,  # 固定数据代表连接请求
            "device": "15689926008",  # 设备标识
            "key": "f015fadb62bd4341a2fb233ab9b02b9b",  # 传输密钥
            "ver": "v1.0"}  # 客户端代码版本号,可以是自己拟定的一组客户端代码版本号值
        try:
            tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket
            tcp_client.connect((host, port))  # 建立tcp连接
            tcp_client.send(json.dumps(handshare_data).encode())  # 发送云平台连接请求
            res_msg = tcp_client.recv(1024).decode()  # 接收云平台响应
        except Exception as e:
            print(e)
            return False
        return tcp_client  # 返回socket对象

    def listen_server(socket_obj):
        '''
        监听TCP连接服务端消息
        :param socket_obj:
        :return:
        '''
        while True:
            try:
                res = socket_obj.recv(1024).decode()  # 接收服务端数据
                if not res:
                    exit()
            except Exception as e:
                print(e)
                exit()

    def send_temperature(tcp_client, num):
        '''

        :param tcp_client: socket对象
        :param num: 体温数据
        :return:
        '''
        if num > 37.3:
            data = {
                "t": 3,  # 固定数字,代表数据上报
                "datatype": 1,  # 数据上报格式类型
                "datas": {
                    "Temprature": num,  # 体温数据
                    "expect_temperature": num,  # 异常体温数据
                },
                "msgid": str(random.randint(100, 100000))  # 消息编号
            }
        else:
            data = {
                "t": 3,
                "datatype": 1,
                "datas": {
                    "Temprature": num,
                },
                "msgid": str(random.randint(100, 100000))
            }
        try:
            tcp_client.send(json.dumps(data).encode())  # 发送数据
        except Exception as e:
            print(e)


if __name__ == '__main__':
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))  # 项目根目录路径
    app = QApplication(sys.argv)
    temp_page = Temper()  # 温度界面调用
    temp_page.show()  # 显示温度界面
    #=====================================================
    tcp_client = socket_client(host, port)  # 创建tcp　sockt 对象
    t1 = Thread(target=listen_server, args=(tcp_client,))  # 监听服务端发送数据
    t1.start()
    t2 = Thread(target=tcp_ping, args=(tcp_client,))  # 创建与云平台保持心跳的线程
    t2.start()
    num = 37.3
    send_temperature(tcp_client, num)  # 发送一条体温数据
    sys.exit(app.exec_())
