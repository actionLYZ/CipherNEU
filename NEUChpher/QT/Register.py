# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Resource.LogResource

import socket
from Socket.Packet import *
import GlobalWindow
from Cipher import MD5

class Ui_register(object):

    def setupUi(self, register_2):
        register_2.setObjectName("register_2")
        register_2.resize(360, 186)
        self.layoutWidget = QtWidgets.QWidget(register_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 184))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lab_nickname = QtWidgets.QLabel(self.layoutWidget)
        self.lab_nickname.setObjectName("lab_nickname")
        self.horizontalLayout.addWidget(self.lab_nickname)
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line_nickname = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_nickname.setObjectName("line_nickname")
        self.horizontalLayout.addWidget(self.line_nickname)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(5, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lab_password = QtWidgets.QLabel(self.layoutWidget)
        self.lab_password.setObjectName("lab_password")
        self.horizontalLayout_2.addWidget(self.lab_password)
        spacerItem2 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.line_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_password.setObjectName("line_password")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.line_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lab_reenter = QtWidgets.QLabel(self.layoutWidget)
        self.lab_reenter.setObjectName("lab_reenter")
        self.horizontalLayout_4.addWidget(self.lab_reenter)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.line_reenter = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_reenter.setObjectName("line_reenter")
        self.line_reenter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_4.addWidget(self.line_reenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.but_register = QtWidgets.QPushButton(self.layoutWidget)
        self.but_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_register.setObjectName("but_register")
        self.horizontalLayout_3.addWidget(self.but_register)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.but_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.but_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_cancel.setObjectName("but_cancel")
        self.horizontalLayout_3.addWidget(self.but_cancel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.listWidget = QtWidgets.QListWidget(register_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 361, 191))
        self.listWidget.setStyleSheet("border-image: url(:/images/background.png);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.raise_()
        self.layoutWidget.raise_()
        self.retranslateUi(register_2)
        self.but_cancel.clicked.connect(register_2.close)
        self.but_register.clicked.connect(self.AddUser)
        QtCore.QMetaObject.connectSlotsByName(register_2)

    def AddUser(self):
        if self.line_nickname.text() == "" or self.line_password.text() == "":
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","用户名或密码不能为空！",QtWidgets.QMessageBox.Yes)

        elif not self.line_nickname.text().isalnum() and self.line_password.text().isalnum():
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","用户名和密码必须由字母与数字组成！",QtWidgets.QMessageBox.Yes)
            '''
            elif self.IfHasRegister():
                message = QtWidgets.QMessageBox()
                message.warning(self,"Error","该用户名已经被注册过了！",QtWidgets.QMessageBox.Yes)
            '''
        elif self.line_password.text() != self.line_reenter.text():
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","两次输入的密码不一致！",QtWidgets.QMessageBox.Yes)

        elif not self.checkBox.isChecked():
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","请勾选NEU协议！",QtWidgets.QMessageBox.Yes)

        else:
            try:
                GlobalWindow.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                GlobalWindow.s.connect((GlobalWindow.host, GlobalWindow.port))
            except socket.error:
                message = QtWidgets.QMessageBox()
                message.warning(self,"Error","无法连接至服务器！",QtWidgets.QMessageBox.Yes)
                return
            if self.AddUser2dir():
                message = QtWidgets.QMessageBox()
                message.information(self,"Pass","注册成功！",QtWidgets.QMessageBox.Yes)
            else:
                GlobalWindow.s.close()
                return
            GlobalWindow.s.close()
            self.close()
    
    #判断用户名是否已经被注册过
    '''
    def IfHasRegister(self):
        document = open("User.txt","a")
        document.close()
        document = open("User.txt","r")
        for context in document.readlines():
            if self.line_nickname.text() == context[:context.find(' ')]:
                document.close()
                return True
        return False
    '''
    #将注册成功的用户登记在User.txt中
    def AddUser2dir(self):
        GlobalWindow.s.sendall(PktToBytes(Packet(TYP_REG, self.line_nickname.text(), b'server', MD5.Encrypt(self.line_password.text()))))
        recv_tmp = GlobalWindow.s.recv(PKT_MAX_SIZE)
        head, sep, rear = recv_tmp.partition(b"<<<<<<")
        pkt = BytesToPkt(head)
        if pkt.typ == TYP_ERR:
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","该用户名已经被注册过了！",QtWidgets.QMessageBox.Yes)
            return False
        elif pkt.typ == TYP_ACK:
            return True
        else:
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","注册异常！请检查服务器设置。",QtWidgets.QMessageBox.Yes)
            return False
        '''
        document = open("User.txt","a")
        document.write(self.line_nickname.text())
        document.write(" ")
        document.write(self.line_password.text())
        document.write("\n")
        document.close()
        '''

    def retranslateUi(self, register_2):
        _translate = QtCore.QCoreApplication.translate
        register_2.setWindowTitle(_translate("register_2", "Register"))
        self.lab_nickname.setText(_translate("register_2", "Nickname"))
        self.lab_password.setText(_translate("register_2", "Password"))
        self.lab_reenter.setText(_translate("register_2", "Re-enter"))
        self.checkBox.setText(_translate("register_2", "I agree NEUrules"))
        self.but_register.setText(_translate("register_2", "Register"))
        self.but_cancel.setText(_translate("register_2", "Cancel"))


#注册窗口对象
class RegisterWindow(QtWidgets.QWidget,Ui_register):  
    def __init__(self):    
        super(RegisterWindow,self).__init__()  
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint)        #只允许最小和关闭，不允许最大化,不允许调整大小
        self.setupUi(self) 
        self.but_register.setDefault(True)
