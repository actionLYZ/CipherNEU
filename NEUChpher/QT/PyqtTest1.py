# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.9

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtGui import QFont, QKeyEvent
import QT.ChatResource
#import Cipher.RSA
import Cipher.Caesar, Cipher.Affine, Cipher.Keyword, Cipher.CA, Cipher.ColumnPermutation, Cipher.DES
import Cipher.DH, Cipher.DoubleTransposition, Cipher.AutokeyPlaintext, Cipher.AutokeyCiphertext, Cipher.MD5
import Cipher.Multiliteral, Cipher.Permutation, Cipher.Playfair, Cipher.RC4, Cipher.Vigenere


def Global():
    global cipherType, encryptKey, decryptKey, plaintext, ciphertext
    cipherType = 'Caesar'
    encryptKey = '12'
    decryptKey = '12'
    plaintext = ''
    ciphertext = ''
    return

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(707, 493)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 671, 453))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(800, 150))
        self.textEdit.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 5, 1, 1, 6)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 4, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(30, 30))
        self.graphicsView.setMaximumSize(QtCore.QSize(100, 100))
        self.graphicsView.setSizeIncrement(QtCore.QSize(0, 0))
        self.graphicsView.setBaseSize(QtCore.QSize(0, 0))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("border-image: url(:/images/user.png);\n"
"border-image: url(:/images/user1.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 6, 1)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 6, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_3 = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_3.setMaximumSize(QtCore.QSize(25, 30))
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setStyleSheet("border-image: url(:/images/lock1.png);")
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.toolButton_2 = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_2.setMaximumSize(QtCore.QSize(25, 30))
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setStyleSheet("border-image: url(:/images/key1.png);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton_4 = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_4.setMaximumSize(QtCore.QSize(25, 30))
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_4.setStyleSheet("border-image: url(:/images/export.png);")
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setMaximumSize(QtCore.QSize(25, 30))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet("border-image: url(:/images/download1.png);")
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 7, 1, 1)
        self.textEdit.raise_()
        self.textBrowser.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 721, 521))
        self.frame.setStyleSheet("background-image: url(:/images/background1.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Encryption"))
        self.comboBox.setItemText(1, _translate("Dialog", "Decryption"))
        self.label_3.setText(_translate("Dialog", "Messages:"))
        self.pushButton_2.setText(_translate("Dialog", "Login"))
        self.pushButton_3.setText(_translate("Dialog", "Register"))
        self.pushButton.setText(_translate("Dialog", "Settings"))
        self.label.setText(_translate("Dialog", "To:"))
        self.label_2.setText(_translate("Dialog", "My messages:"))
        self.toolButton_3.setText(_translate("Dialog", ""))
        self.toolButton_2.setText(_translate("Dialog", ""))
        self.toolButton_4.setText(_translate("Dialog", ""))
        self.toolButton.setText(_translate("Dialog", ""))
        self.pushButton_4.setText(_translate("Dialog", "Show Ciphertext"))
        self.pushButton_8.setText(_translate("Dialog", "Send"))

class mywindow(QtWidgets.QWidget,Ui_Dialog):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self) 
        self.initUI()
        self.pushButton_8.clicked.connect(self.EncryptPrint)
        self.pushButton_4.clicked.connect(self.ShowMessage)
        self.toolButton_3.clicked.connect(self.ShowMessage)
        #self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)   
        #self.pushButton.clicked.connect(self.EncryptPrint)
        #self.pushButton_3.clicked.connect(self.DecryptPrint)

    def initUI(self): 
        QToolTip.setFont(QFont('SansSerif', 10)) 
        self.toolButton_3.setToolTip('encryption setting')
        self.toolButton_2.setToolTip('decryption setting')
        self.toolButton_4.setToolTip('export file')
        self.toolButton.setToolTip('download file')
        #self.pushButton_4.setToolTip(self.textEdit.toPlainText())

    def ShowMessage(self):
        message = QtWidgets.QMessageBox()
        str = self.textEdit.toPlainText()
        l = len(self.textEdit.toPlainText())
        for i in range(int(l/20)):
            str = str[:i*22+20]+'\n'+str[i*22+20:]
        message.information(self,"Ciphertext",str)

    def keyPressEvent(self,QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            #self.textEdit.setToolTip('aaa')
            print('aaa')
        return super().keyPressEvent(QKeyEvent)

    def EncryptPrint(self):
        if(self.comboBox.currentText()=='Encryption'):
            self.Encryption()
        elif(self.comboBox.currentText()=='Decryption'):
            self.Decryption()
    def Encryption(self):
        Global()
        plaintext = self.textEdit.toPlainText()
        self.textBrowser.setText(self.textBrowser.toPlainText()+'Plaintext: '+plaintext+'\n'+'Ciphertext: '+Caesar.Encrypt(plaintext,int(encryptKey))+'\n\n')

    def Decryption(self):
        Global()
        ciphertext = self.textEdit.toPlainText()
        self.textBrowser.setText(self.textBrowser.toPlainText()+'Ciphertext: '+ciphertext+'\n'+'Plaintext: '+Caesar.Decrypt(ciphertext,int(decryptKey))+'\n\n')

if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()  
    myshow.show()
    sys.exit(app.exec_())