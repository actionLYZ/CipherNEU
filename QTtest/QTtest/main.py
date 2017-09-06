# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  sys  


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(491, 348)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(110, 230, 261, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(50)
        self.splitter.setObjectName("splitter")
        self.encrypt = QtWidgets.QPushButton(self.splitter)
        self.encrypt.setObjectName("encrypt")
        self.MyButton = QtWidgets.QPushButton(self.splitter)
        self.MyButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.MyButton.setObjectName("MyButton")
        self.tb = QtWidgets.QTextBrowser(Form)
        self.tb.setGeometry(QtCore.QRect(120, 20, 256, 192))
        self.tb.setObjectName("tb")
        self.retranslateUi(Form)

        self.MyButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.encrypt.setText(_translate("Form", "加密"))
        self.MyButton.setText(_translate("Form", "quit"))

