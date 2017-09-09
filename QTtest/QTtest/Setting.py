# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Setting.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(360, 189)
        self.layoutWidget = QtWidgets.QWidget(Setting)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 341, 162))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lab_IP = QtWidgets.QLabel(self.layoutWidget)
        self.lab_IP.setObjectName("lab_IP")
        self.horizontalLayout_4.addWidget(self.lab_IP)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.lineIp = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineIp.setObjectName("lineIp")
        self.horizontalLayout_4.addWidget(self.lineIp)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.lab_Port = QtWidgets.QLabel(self.layoutWidget)
        self.lab_Port.setObjectName("lab_Port")
        self.horizontalLayout_5.addWidget(self.lab_Port)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.line_Port = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_Port.setObjectName("line_Port")
        self.horizontalLayout_5.addWidget(self.line_Port)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.but_login = QtWidgets.QPushButton(self.layoutWidget)
        self.but_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_login.setObjectName("but_login")
        self.horizontalLayout_6.addWidget(self.but_login)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.background = QtWidgets.QListWidget(Setting)
        self.background.setGeometry(QtCore.QRect(0, 0, 371, 201))
        self.background.setStyleSheet("border-image: url(:/images/background.png);")
        self.background.setObjectName("background")
        self.background.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Setting"))
        self.lab_IP.setText(_translate("Setting", "Server IP"))
        self.lab_Port.setText(_translate("Setting", "Server Port"))
        self.but_login.setText(_translate("Setting", "Enter"))

import resource

#设置窗口对象
class SettingWindow(QtWidgets.QWidget,Ui_Setting):  
    def __init__(self):    
        super(SettingWindow,self).__init__()  
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint)        #只允许最小和关闭，不允许最大化,不允许调整大小
        self.setupUi(self)  