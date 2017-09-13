# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncryptionSetting.ui'
#
# Created by: PyQt5 UI code generator 5.9

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import Resource.LogResource
import GlobalWindow

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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
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
        Dialog.setWindowTitle(_translate("Dialog", "Encryption Setting"))
        self.label_2.setText(_translate("Dialog", "Encryption Algorithm:"))
        self.comboBox.setItemText(0, _translate("Dialog", "None"))
        self.comboBox.setItemText(1, _translate("Dialog", "Caesar"))
        self.comboBox.setItemText(2, _translate("Dialog", "Affine"))
        self.comboBox.setItemText(3, _translate("Dialog", "Keyword"))
        self.comboBox.setItemText(4, _translate("Dialog", "Multiliteral"))
        self.comboBox.setItemText(5, _translate("Dialog", "Vigenere"))
        self.comboBox.setItemText(6, _translate("Dialog", "Autokey Ciphertext"))
        self.comboBox.setItemText(7, _translate("Dialog", "Autokey Plaintext"))
        self.comboBox.setItemText(8, _translate("Dialog", "Playfair"))
        self.comboBox.setItemText(9, _translate("Dialog", "Permutation"))
        self.comboBox.setItemText(10, _translate("Dialog", "Column Permutation"))
        self.comboBox.setItemText(11, _translate("Dialog", "Double Transposition"))
        self.comboBox.setItemText(12, _translate("Dialog", "RC4"))
        self.comboBox.setItemText(13, _translate("Dialog", "CA"))
        self.comboBox.setItemText(14, _translate("Dialog", "DES"))
        self.comboBox.setItemText(15, _translate("Dialog", "AES-128"))
        self.comboBox.setItemText(16, _translate("Dialog", "AES-192"))
        self.comboBox.setItemText(17, _translate("Dialog", "AES-256"))
        self.comboBox.setItemText(18, _translate("Dialog", "RSA"))
        self.comboBox.setItemText(19, _translate("Dialog", "ECC"))
        self.comboBox.setItemText(20, _translate("Dialog", "MD5"))
        #self.comboBox.setItemText(21, _translate("Dialog", "DSA"))
        #self.comboBox.setItemText(22, _translate("Dialog", "DH"))
        self.label.setText(_translate("Dialog", "Secret Key:"))
        self.comboBox.setCurrentText(_translate("Dialog", GlobalWindow.enCipherType))
        self.lineEdit.setText(_translate("Dialog", GlobalWindow.encryptKey))


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
        self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
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
        Dialog.setWindowTitle(_translate("Dialog", "Decryption Setting"))
        self.comboBox.setItemText(0, _translate("Dialog", "None"))
        self.comboBox.setItemText(1, _translate("Dialog", "Caesar"))
        self.comboBox.setItemText(2, _translate("Dialog", "Affine"))
        self.comboBox.setItemText(3, _translate("Dialog", "Keyword"))
        self.comboBox.setItemText(4, _translate("Dialog", "Multiliteral"))
        self.comboBox.setItemText(5, _translate("Dialog", "Vigenere"))
        self.comboBox.setItemText(6, _translate("Dialog", "Autokey Ciphertext"))
        self.comboBox.setItemText(7, _translate("Dialog", "Autokey Plaintext"))
        self.comboBox.setItemText(8, _translate("Dialog", "Playfair"))
        self.comboBox.setItemText(9, _translate("Dialog", "Permutation"))
        self.comboBox.setItemText(10, _translate("Dialog", "Column Permutation"))
        self.comboBox.setItemText(11, _translate("Dialog", "Double Transposition"))
        self.comboBox.setItemText(12, _translate("Dialog", "RC4"))
        self.comboBox.setItemText(13, _translate("Dialog", "CA"))
        self.comboBox.setItemText(14, _translate("Dialog", "DES"))
        self.comboBox.setItemText(15, _translate("Dialog", "AES-128"))
        self.comboBox.setItemText(16, _translate("Dialog", "AES-192"))
        self.comboBox.setItemText(17, _translate("Dialog", "AES-256"))
        self.comboBox.setItemText(18, _translate("Dialog", "RSA"))
        self.comboBox.setItemText(19, _translate("Dialog", "ECC"))
        #self.comboBox.setItemText(20, _translate("Dialog", "MD5"))
        #self.comboBox.setItemText(21, _translate("Dialog", "DSA"))
        #self.comboBox.setItemText(22, _translate("Dialog", "DH"))
        self.label.setText(_translate("Dialog", "Secret Key:"))
        self.label_2.setText(_translate("Dialog", "Decryption Algorithm:"))
        self.comboBox.setCurrentText(_translate("Dialog", GlobalWindow.deCipherType))
        self.lineEdit.setText(_translate("Dialog", GlobalWindow.decryptKey))

class EncryptionSettingWindow(QtWidgets.QWidget,En_Ui_Dialog):    
    def __init__(self):    
        super(EncryptionSettingWindow,self).__init__()    
        self.setupUi(self) 
        #self.SetExample()
        self.buttonBox.accepted.connect(self.Accept)
        self.buttonBox.rejected.connect(self.close)
        self.comboBox.currentTextChanged.connect(self.SetExample)
        #self.comboBox.activated.connect(self.SetExample)
        if GlobalWindow.enCipherType == "None":
            self.lineEdit.setDisabled(True)

    def SetExample(self):
        self.lineEdit.setDisabled(False)
        if (self.comboBox.currentText()=='None'):
            self.lineEdit.setText('')
            self.lineEdit.setDisabled(True)
        elif(self.comboBox.currentText()=='Caesar'):
            self.lineEdit.setText('3')
        elif(self.comboBox.currentText()=='Affine'):
            self.lineEdit.setText('3 1')
        elif(self.comboBox.currentText()=='Double Transposition'):
            self.lineEdit.setText('hello world')
        elif(self.comboBox.currentText()=='CA'):
            self.lineEdit.setText('23')
        elif(self.comboBox.currentText()=='DES'):
            self.lineEdit.setText('abcdefgh')
        elif self.comboBox.currentText() in ["Keyword", "Multiliteral", "Vigenere", "Autokey Ciphertext", "Autokey Plaintext", "Playfair", "Permutation", "Column Permutation"]:
            self.lineEdit.setText("hello")
        
    # Check out if the key is valid, such as AES-128(16 bytes), AES-192(24 bytes), AES-256(32 bytes), etc.
    def IsValid(self,key, type):
        if type == "None":
            return True
        elif type == "Caesar":
            if key.isdigit():
                if int(key) > 0 and int(key) < 26:
                    return True
        elif type == "DES":
            return key.isalpha() and len(key)==8
        elif type == "Affine":
            if(' ' not in key):
                return False
            for i in range(len(key)):
                if(key[i]==' '):
                    a = key[:i]
                    b = key[i+1:]
                    break
                i = i+1
            if(a.isdigit() and b.isdigit()):
                if((0<int(a)<26)&(0<int(b)<26)):
                    return True
        elif type == "Double Transposition":
            key = key.split()
            if(key[0].isalpha() and key[1].isalpha()):
                return True
        elif type == "RC4":
            return isinstance(key, str)
        elif type == "AES-128":
            return isinstance(key, str) and len(key) == 16
        elif type == "AES-192":
            return isinstance(key, str) and len(key) == 24
        elif type == "AES-256":
            return isinstance(key, str) and len(key) == 32
        elif type =='CA':
            return key.isdigit()
        elif ["Keyword", "Multiliteral", "Vigenere", "Autokey Ciphertext", "Autokey Plaintext", "Playfair", "Permutation", "Column Permutation"].index(type) != -1:
            return isinstance(key, str) and key.isalpha()
        return False

    def Accept(self):
        if(self.IsValid(self.lineEdit.text(),self.comboBox.currentText()) == False):
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","Wrong Secretkey Format!",QtWidgets.QMessageBox.Ok)
            message.close()
        else:
            GlobalWindow.enCipherType = self.comboBox.currentText()
            GlobalWindow.encryptKey = self.lineEdit.text()
            self.close()


class DecryptionSettingWindow(QtWidgets.QWidget,De_Ui_Dialog):    
    def __init__(self):    
        super(DecryptionSettingWindow,self).__init__()    
        self.setupUi(self) 
        self.buttonBox.accepted.connect(self.Accept)
        self.buttonBox.clicked.connect(self.close)
        self.comboBox.activated.connect(self.SetExample)
        if GlobalWindow.deCipherType == "None":
            self.lineEdit.setDisabled(True)

    def SetExample(self):
        self.lineEdit.setDisabled(False)
        if (self.comboBox.currentText()=='None'):
            self.lineEdit.setText('')
            self.lineEdit.setDisabled(True)
        elif(self.comboBox.currentText()=='Caesar'):
            self.lineEdit.setText('3')
        elif(self.comboBox.currentText()=='Affine'):
            self.lineEdit.setText('3 1')
        elif(self.comboBox.currentText()=='Double Transposition'):
            self.lineEdit.setText('hello world')
        elif(self.comboBox.currentText()=='CA'):
            self.lineEdit.setText('23')
        elif(self.comboBox.currentText()=='DES'):
            self.lineEdit.setText('abcdefgh')
        elif self.comboBox.currentText() in ["Keyword", "Multiliteral", "Vigenere", "Autokey Ciphertext", "Autokey Plaintext", "Playfair", "Permutation", "Column Permutation"]:
            self.lineEdit.setText("hello")
        

    def IsValid(self,key, type):
        if type == "None":
            return True
        elif type == "Caesar":
            if key.isdigit():
                if int(key) > 0 and int(key) < 26:
                    return True
        elif type == "DES":
            return key.isalpha() and len(key)==8
        elif type == "Affine":
            if(' ' not in key):
                return False
            for i in range(len(key)):
                if(key[i]==' '):
                    a = key[:i]
                    b = key[i+1:]
                    break
                i = i+1
            if(a.isdigit() and b.isdigit()):
                if((0<int(a)<26)&(0<int(b)<26)):
                    return True
        elif type == "Double Transposition":
            key = key.split()
            if(key[0].isalpha() and key[1].isalpha()):
                return True
        elif type == "RC4":
            return isinstance(key, str)
        elif type == "AES-128":
            return isinstance(key, str) and len(key) == 16
        elif type == "AES-192":
            return isinstance(key, str) and len(key) == 24
        elif type == "AES-256":
            return isinstance(key, str) and len(key) == 32
        elif ["Keyword", "Multiliteral", "Vigenere", "Autokey Ciphertext", "Autokey Plaintext", "Playfair", "Permutation", "Column Permutation"].index(type) != -1:
            return isinstance(key, str) and key.isalpha()
        return False

    def Accept(self):
        if(self.IsValid(self.lineEdit.text(),self.comboBox.currentText())==False):
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","Wrong Secretkey Format!",QtWidgets.QMessageBox.Ok)
            message.close()
        else:
            GlobalWindow.deCipherType = self.comboBox.currentText()
            GlobalWindow.decryptKey = self.lineEdit.text()
            self.close()
