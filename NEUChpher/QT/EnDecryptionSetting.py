# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncryptionSetting.ui'
#
# Created by: PyQt5 UI code generator 5.9

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import Resource.LogResource

enCipherType = ''
deCipherType = ''
encryptKey = ''
decryptKey = ''

class En_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 190)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 321, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-30, -10, 441, 201))
        self.frame.setStyleSheet("background-image: url(:/images/background.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Encryption Algorithm:"))
        self.comboBox.setItemText(0, _translate("Dialog", "Caesar"))
        self.comboBox.setItemText(1, _translate("Dialog", "Affine"))
        self.comboBox.setItemText(2, _translate("Dialog", "Keyword"))
        self.comboBox.setItemText(3, _translate("Dialog", "Multiliteral"))
        self.comboBox.setItemText(4, _translate("Dialog", "Vigenere"))
        self.comboBox.setItemText(5, _translate("Dialog", "Autokey Ciphertext"))
        self.comboBox.setItemText(6, _translate("Dialog", "Autokey Plaintext"))
        self.comboBox.setItemText(7, _translate("Dialog", "Playfair"))
        self.comboBox.setItemText(8, _translate("Dialog", "Permutation"))
        self.comboBox.setItemText(9, _translate("Dialog", "Column Permutation"))
        self.comboBox.setItemText(10, _translate("Dialog", "Double Transposition"))
        self.comboBox.setItemText(11, _translate("Dialog", "RC4"))
        self.comboBox.setItemText(12, _translate("Dialog", "CA"))
        self.comboBox.setItemText(13, _translate("Dialog", "DES"))
        self.comboBox.setItemText(14, _translate("Dialog", "AES"))
        self.comboBox.setItemText(15, _translate("Dialog", "RSA"))
        self.comboBox.setItemText(16, _translate("Dialog", "ECC"))
        self.comboBox.setItemText(17, _translate("Dialog", "MD5"))
        self.comboBox.setItemText(18, _translate("Dialog", "DSA"))
        self.comboBox.setItemText(19, _translate("Dialog", "DH"))
        self.label.setText(_translate("Dialog", "Secret Key:"))


class De_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 189)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 321, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, -10, 421, 211))
        self.frame.setStyleSheet("background-image: url(:/images/background.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Caesar"))
        self.comboBox.setItemText(1, _translate("Dialog", "Affine"))
        self.comboBox.setItemText(2, _translate("Dialog", "Keyword"))
        self.comboBox.setItemText(3, _translate("Dialog", "Multiliteral"))
        self.comboBox.setItemText(4, _translate("Dialog", "Vigenere"))
        self.comboBox.setItemText(5, _translate("Dialog", "Autokey Ciphertext"))
        self.comboBox.setItemText(6, _translate("Dialog", "Autokey Plaintext"))
        self.comboBox.setItemText(7, _translate("Dialog", "Playfair"))
        self.comboBox.setItemText(8, _translate("Dialog", "Permutation"))
        self.comboBox.setItemText(9, _translate("Dialog", "Column Permutation"))
        self.comboBox.setItemText(10, _translate("Dialog", "Double Transposition"))
        self.comboBox.setItemText(11, _translate("Dialog", "RC4"))
        self.comboBox.setItemText(12, _translate("Dialog", "CA"))
        self.comboBox.setItemText(13, _translate("Dialog", "DES"))
        self.comboBox.setItemText(14, _translate("Dialog", "AES"))
        self.comboBox.setItemText(15, _translate("Dialog", "RSA"))
        self.comboBox.setItemText(16, _translate("Dialog", "ECC"))
        self.comboBox.setItemText(17, _translate("Dialog", "MD5"))
        self.comboBox.setItemText(18, _translate("Dialog", "DSA"))
        self.comboBox.setItemText(19, _translate("Dialog", "DH"))
        self.label.setText(_translate("Dialog", "Secret Key:"))
        self.label_2.setText(_translate("Dialog", "Decryption Algorithm:"))

class EncryptionSettingWindow(QtWidgets.QWidget,En_Ui_Dialog):    
    def __init__(self):    
        super(EncryptionSettingWindow,self).__init__()    
        self.setupUi(self) 
        self.buttonBox.accepted.connect(self.Accept)
        self.buttonBox.clicked.connect(self.close)
    def Accept(self):
        global encryptKey,enCipherType
        enCipherType = self.comboBox.currentText()
        encryptKey = self.lineEdit.text()

class DecryptionSettingWindow(QtWidgets.QWidget,De_Ui_Dialog):    
    def __init__(self):    
        super(DecryptionSettingWindow,self).__init__()    
        self.setupUi(self) 
        self.buttonBox.accepted.connect(self.Accept)
        self.buttonBox.clicked.connect(self.close)
    def Accept(self):
        global decryptKey,deCipherType
        deCipherType = self.comboBox.currentText()
        decryptKey = self.lineEdit.text()



