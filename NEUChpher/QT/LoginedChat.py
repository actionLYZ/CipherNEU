# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.9

from PyQt5 import QtCore, QtGui, QtWidgets
import Resource.LogedResource,Resource.TitleResource
import GlobalWindow
from QT import Login,Register,Setting,FilePath,LoginedChat,EnDecryptionSetting,LoginedChat
from Cipher import RSA, DSA, ECC
from Cipher import Caesar, Affine, Keyword, CA, ColumnPermutation, DES, DoubleTransposition, AutokeyPlaintext, AutokeyCiphertext, MD5, Multiliteral, Permutation, Playfair, RC4, Vigenere, AES
from Socket.Packet import *
from Cipher import Python
#from UKey.UKey import *

import socket, _thread, time, random

class Ui_Dialog(object):
    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(707, 493)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
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
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(200, 60))
        self.label_4.setText("")
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Lucida Handwriting\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        #self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        #self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        #self.pushButton.setObjectName("pushButton")
        #self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setSizeIncrement(QtCore.QSize(100, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
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

        Dialog.setWindowTitle(_translate("Dialog", "NEUCryptolalia"))
        #self.label_4.setText(_translate("Dialog", "Welcome!\n"))
        self.comboBox.setItemText(0, _translate("Dialog", "Plaintext"))
        self.comboBox.setItemText(1, _translate("Dialog", "Ciphertext"))
        self.label_3.setText(_translate("Dialog", "Messages:"))
        #self.pushButton.setText(_translate("Dialog", "Settings"))
        self.pushButton_2.setText(_translate("Dialog", "Logout"))
        self.label.setText(_translate("Dialog", "To:"))
        self.label_2.setText(_translate("Dialog", "My messages:"))
        self.toolButton_3.setText(_translate("Dialog", "   "))
        self.toolButton_2.setText(_translate("Dialog", "   "))
        self.toolButton_4.setText(_translate("Dialog", "   "))
        self.toolButton.setText(_translate("Dialog", "   "))
        self.pushButton_4.setText(_translate("Dialog", "Preview"))
        self.pushButton_8.setText(_translate("Dialog", "Send"))

#登陆窗口对象
class LoginedChatWindow(QtWidgets.QWidget,Ui_Dialog):  
    filetext = ''
    content = ''
    toPersonName = ''

    def __init__(self):    
        super(LoginedChatWindow,self).__init__()    
        self.logedWindow = None
        self.loginWindow=None
        self.setupUi(self) 
        self.DisplayTip()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint )        #只允许最小和关闭，不允许最大化,不允许调整大小
        #控件映射
        self.pushButton_8.clicked.connect(self.Send)
        self.pushButton_4.clicked.connect(self.ShowMessage)
        #self.pushButton.clicked.connect(self.OpenSettingWindows)
        self.pushButton_2.clicked.connect(self.Logout)
        self.toolButton_3.clicked.connect(self.OpenEncryptionSettingWindows)
        self.toolButton_2.clicked.connect(self.OpenDecryptionSettingWindows)
        self.toolButton_4.clicked.connect(self.ReadFile)
        self.toolButton.clicked.connect(self.SaveFile)
        
    #显示悬停提示
    def DisplayTip(self): 
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10)) 
        self.toolButton_3.setToolTip('encryption setting')
        self.toolButton_2.setToolTip('decryption setting')
        self.toolButton_4.setToolTip('export file')
        self.toolButton.setToolTip('download file')

    #读取文件
    def ReadFile(self):
        openFile = QtWidgets.QFileDialog()
        self.path, filetype = openFile.getOpenFileName(self,  
                                    "选取文件",  
                                    "C:/",  
                                    "Text Files (*.txt)")   
        if self.path != '':
            GlobalWindow.uploadPath = self.path
            document = open(self.path,"r")
            self.content = document.readlines()
            self.content = ''.join(self.content)
            self.textEdit.setText(self.content)
            GlobalWindow.isFile = True
            document.close()

    #保存文件
    def SaveFile(self):
        savefile = QtWidgets.QFileDialog()
        filepath,filetype= savefile.getSaveFileName(self,  
                                    "文件保存",  
                                    "C:/",
                                    "Text Files (*.txt)")
        if filepath != '':
            document = open(filepath,"w+")
            document.write(GlobalWindow.filedata)
            document.close()

    #打印双机加密信息
    def ShowMessage(self):
        message = QtWidgets.QMessageBox()
        beforeStr = '----------- CipherText -----------\n'
        str = self.textEdit.toPlainText()
        if(str==''):
            str = 'None'
        if self.comboBox.currentText() == "Ciphertext":
            str = self.DefineCipherType(str, 0)
        length = len(str)
        wideth = int(length * (3/5))
        if wideth < 15:
            wideth = 15
        spacenum = (34 - wideth) // 2
        spacestr = ' ' * spacenum
        for i in range(int(length/wideth)):
            str = spacestr + str[:i*22+wideth]+'\n'+spacestr + str[i*22+wideth:]
        if length/wideth < 1:
            str = spacestr +str[:]
        str = beforeStr + str[:]
        message.about(self,"Preview",str)

    #发送
    def Send(self):
        if not GlobalWindow.isFile:
            plaintext = self.textEdit.toPlainText()
            if plaintext == "":
                message = QtWidgets.QMessageBox()
                message.warning(self,"Error","内容不能为空！",QtWidgets.QMessageBox.Ok)
                return
            if self.comboBox.currentText() == "Plaintext":
                self.writeToTextBrowser(GlobalWindow.username.decode() + ": " + plaintext)
                pkt = Packet(TYP_PTX, GlobalWindow.username, self.lineEdit.text(), plaintext)
                GlobalWindow.s.sendall(PktToBytes(pkt))
            else:
                ciphertext = self.DefineCipherType(plaintext, 0)
                self.writeToTextBrowser(GlobalWindow.username.decode() + ": " + ciphertext + " (Plaintext: " + plaintext + ")")
                pkt = Packet(TYP_CTX, GlobalWindow.username, self.lineEdit.text(), ciphertext)
                GlobalWindow.s.sendall(PktToBytes(pkt))
        else:
            plaintext = self.readFile(GlobalWindow.uploadPath)
            if self.comboBox.currentText() == "Plaintext":
                if GlobalWindow.enCipherType == "DSA":
                    #print("1")
                    plaintext = self.DSA_SignProcess()
                temp, sep, name = GlobalWindow.uploadPath.rpartition("/")
                data = name.encode() + b">>>>>>" + plaintext.encode()
                self.writeToTextBrowser(GlobalWindow.username.decode() + ": (Send file: " + name + ")")
                pkt = Packet(TYP_PFL, GlobalWindow.username, self.lineEdit.text(), data)
                GlobalWindow.s.sendall(PktToBytes(pkt))
            else:
                ciphertext = self.DefineCipherType(plaintext, 0)
                temp, sep, name = GlobalWindow.uploadPath.rpartition("/")
                data = name.encode() + b">>>>>>" + ciphertext.encode()
                self.writeToTextBrowser(GlobalWindow.username.decode() + ": (Send file: " + name + ", encrypted)")
                pkt = Packet(TYP_CFL, GlobalWindow.username, self.lineEdit.text(), data)
                GlobalWindow.s.sendall(PktToBytes(pkt))
            GlobalWindow.isFile = False
        self.textEdit.setText("")

    #DSA方式发送文件处理
    def DSA_SignProcess(self):
        #print("2")
        plaintext = self.readFile(GlobalWindow.uploadPath)
        key = Python.Read_From()
        # key = (45765342401604687241128449772944733752990916022564027455790382055746256400541598197068931346511522461150446895744952616520086278134132978832871916005779068152320248430961052271558801557201924112195543438798171388390044569701508878757507381031997085133554835541412574591824296504065160930628980769756859931990,43376379741515098647985425804924879601418733263383850422598111312577593386358487364224325263259858969597179251430700334177085086070671449464377616596274930686913256608398943997830334161922260743497953638415364436460427838759705357463553196755185148779782007128058722284120672980828831033776489898432828082361,89884656743115797203643969326208167354925714643588468712364745929920911611342304769134404976757706776492814888985130026442956403037161947081508067139935189302454456558696954436501574072984903785582353419756739807211841909524953510682258535758101581242581094790592743585216465460932752002047977201839275936987,935386979343325361212450472438835748446251696899)
        #key = Read_From()

        key = list(key)
        key.append(157431932338196084657629305270682047200580952750)
        key = tuple(key)
        sig_str = DSA.Sign(plaintext,key) 
        plaintext = plaintext + '>>>>>>' + sig_str
        return plaintext

    #根据不同加解密类型加解密
    def DefineCipherType(self,text,endeMode):      #endeMode = 0 -> encryption/ endeMode = 1 -> decryption
        Text = ''
        if(endeMode==0):
            if GlobalWindow.enCipherType == "None":
                Text = text
            elif(GlobalWindow.enCipherType=='Caesar'):
                Text = Caesar.Encrypt(text,int(GlobalWindow.encryptKey))
            elif(GlobalWindow.enCipherType=='Affine'):
                Text = Affine.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Keyword'):
                Text = Keyword.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Multiliteral'):
                Text = Multiliteral.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Vigenere'):
                Text = Vigenere.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Autokey Ciphertext'):
                Text = AutokeyCiphertext.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Autokey Plaintext'):
                Text = AutokeyPlaintext.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Playfair'):
                Text = Playfair.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Permutation'):
                Text = Permutation.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Column Permutation'):
                Text = ColumnPermutation.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='Double Transposition'):
                Text = DoubleTransposition.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='RC4'):
                Text = RC4.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='CA'):
                Text = CA.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='DES'):
                Text = DES.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='AES-128' or GlobalWindow.enCipherType=='AES-192' or GlobalWindow.enCipherType=='AES-256'):
                Text = AES.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='RSA'):
                Text = RSA.Encrypt(text)
            #elif(GlobalWindow.enCipherType=='ECC'):
                #Text = ECC.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.enCipherType=='MD5'):
                Text = MD5.Encrypt(text)
            elif(GlobalWindow.enCipherType=='DSA'):
                Text = DSA.Encrypt(text,GlobalWindow.encryptKey)
            #elif(GlobalWindow.enCipherType=='DH'):
                #Text = DH.Encrypt(text,GlobalWindow.encryptKey)
        elif(endeMode==1):
            if GlobalWindow.deCipherType == "None":
                Text = text
            elif(GlobalWindow.deCipherType=='Caesar'):
                Text = Caesar.Decrypt(text,int(GlobalWindow.decryptKey))
            elif(GlobalWindow.deCipherType=='Affine'):
                Text = Affine.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Keyword'):
                Text = Keyword.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Multiliteral'):
                Text = Multiliteral.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Vigenere'):
                Text = Vigenere.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Autokey Ciphertext'):
                Text = AutokeyCiphertext.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Autokey Plaintext'):
                Text = AutokeyPlaintext.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Playfair'):
                Text = Playfair.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Permutation'):
                Text = Permutation.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Column Permutation'):
                Text = ColumnPermutation.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='Double Transposition'):
                Text = DoubleTransposition.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='RC4'):
                Text = RC4.Decrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='CA'):
                Text = CA.Encrypt(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.deCipherType=='DES'):
                DES.DESDecryption(text,GlobalWindow.decryptKey)
            elif(GlobalWindow.enCipherType=='AES-128'or GlobalWindow.enCipherType=='AES-192' or GlobalWindow.enCipherType=='AES-256'):
                Text = AES.Encrypt(text,GlobalWindow.encryptKey)
            elif(GlobalWindow.deCipherType=='RSA'):
                Text = RSA.Decrypt(text)
            #elif(GlobalWindow.deCipherType=='ECC'):
                #Text = ECC.Decrypt(text,GlobalWindow.decryptKey)
            #elif(GlobalWindow.deCipherType=='MD5'):
                #Text = MD5.Decrypt(text)
            elif(GlobalWindow.deCipherType=='DSA'):
                Text = DSA.Decrypt(text,GlobalWindow.decryptKey)
            #elif(GlobalWindow.deCipherType=='DH'):
                #Text = DH.Decrypt(text,GlobalWindow.decryptKey)
        return Text 

    #打开加密设置窗口
    def OpenEncryptionSettingWindows(self):
        self.EnSettingWindows = EnDecryptionSetting.EncryptionSettingWindow()
        self.EnSettingWindows.show()

    #打开解密设置窗口
    def OpenDecryptionSettingWindows(self):
        self.DeSettingWindows = EnDecryptionSetting.DecryptionSettingWindow()
        self.DeSettingWindows.show()

    #退出已登录窗口
    def Logout(self):
        GlobalWindow.s.sendall(PktToBytes(Packet(TYP_LOO, GlobalWindow.username, b'server', b'')))
        message = QtWidgets.QMessageBox()
        message.information(self,"Pass","登出成功！",QtWidgets.QMessageBox.Yes)
        GlobalWindow.s.close()
        GlobalWindow.globalWindow.chatwindow.show()
        self.close()

    def writeToTextBrowser(self, str):
        self.textBrowser.insertPlainText("[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "]" + str + "\n")
        vb = self.textBrowser.verticalScrollBar() 
        vb.setValue(vb.maximum()) 
        return

    def showEvent(self, QShowEvent):
        _thread.start_new_thread(self.recvThread, ())
        return super().showEvent(QShowEvent)

    def packetProcess(self, bys):
        head, sep, rear = bys.partition(b"<<<<<<")
        pkt = BytesToPkt(head)
        if pkt.typ == TYP_PTX:
            self.writeToTextBrowser(pkt.src.decode() + ": " + pkt.data.decode())
        elif pkt.typ == TYP_LOO:
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error",pkt.data.decode(),QtWidgets.QMessageBox.Ok)
            GlobalWindow.s.close()
            GlobalWindow.globalWindow.chatwindow.show()
            self.close()
            if (rear != b""):
                self.packetProcess(rear);
            return
        elif pkt.typ == TYP_KEY:
            if pkt.src == b"server":
                GlobalWindow.keylist = {}
                ps, sep, gs = pkt.data.decode().partition(">>>>>>")
                GlobalWindow.p = int(ps)
                GlobalWindow.g = int(gs)
                GlobalWindow.key = random.randint(0, GlobalWindow.p - 1)
                GlobalWindow.s.sendall(PktToBytes(Packet(TYP_KEY, GlobalWindow.username, b"server", str(ECC.fast_pow(GlobalWindow.g, GlobalWindow.key, GlobalWindow.p)))))
                self.writeToTextBrowser("(Get DH: p = " + str(GlobalWindow.p) + ", g = " + str(GlobalWindow.g) + ", key = " + str(GlobalWindow.key) + ")")
            else:
                GlobalWindow.keylist[pkt.src] = ECC.fast_pow(int(pkt.data.decode()), GlobalWindow.key, GlobalWindow.p)
                self.writeToTextBrowser("(Get DH: Key from " + pkt.src.decode() + ", recvkey = " + pkt.data.decode() + ", gab = " + str(GlobalWindow.keylist[pkt.src]) + ")")
        elif pkt.typ == TYP_CTX:
            plaintext = self.DefineCipherType(pkt.data.decode(), 1)
            self.writeToTextBrowser(pkt.src.decode() + ": " + pkt.data.decode() + " (Plaintext: " + plaintext + ")")
        elif pkt.typ == TYP_PFL:
            name, sep, data = pkt.data.decode().partition(">>>>>>")
            if ">>>>>>" in data:
                #print("3")
                data = self.DSA_VerifyProcess(data)
                if data == False:
                    self.writeToTextBrowser(pkt.src.decode() + ": (Receive file: " + name + "), DSA Verify fail!")
                    if (rear != b""):
                        self.packetProcess(rear);
                    return
            path = DOWNLOAD_PATH + name
            downloadPath = path
            #self.writeFile(path, data)
            #temp, sep, GlobalWindow.filetype = name.rpartition(".")
            GlobalWindow.filedata = data
            self.writeToTextBrowser(pkt.src.decode() + ": (Receive file: " + name + ")")
            self.SaveFile()
            #message = QtWidgets.QMessageBox()
            #message.information(self,"Pass","已接收到明文文件，请下载！",QtWidgets.QMessageBox.Yes)
        elif pkt.typ == TYP_CFL:
            name, sep, data = pkt.data.decode().partition(">>>>>>")
            path = DOWNLOAD_PATH + name
            downloadPath = path
            #self.writeFile(path, self.DefineCipherType(data, 1))
            #temp, sep, GlobalWindow.filetype = name.rpartition(".")
            GlobalWindow.filedata = data
            GlobalWindow.fileIsEncrypted = True
            self.writeToTextBrowser(pkt.src.decode() + ": (Receive file: " + name + ", encrypted)")
            #message = QtWidgets.QMessageBox()
            #message.information(self,"Pass","已接收到密文文件，请下载！",QtWidgets.QMessageBox.Yes)
            self.SaveFile()
        else:
            print(recv_tmp.decode())
        if (rear != b""):
            self.packetProcess(rear);
        return

    def recvThread(self):
        while True:
            try:
                recv_tmp = GlobalWindow.s.recv(PKT_MAX_SIZE)
                if not recv_tmp:
                    return
                self.packetProcess(recv_tmp)
            except socket.error:
                break

    #DSA方式传输文件接收处理
    def DSA_VerifyProcess(self, data):
        #print("4")
        data, sep, sig_str = data.partition(">>>>>>")
        key = (45765342401604687241128449772944733752990916022564027455790382055746256400541598197068931346511522461150446895744952616520086278134132978832871916005779068152320248430961052271558801557201924112195543438798171388390044569701508878757507381031997085133554835541412574591824296504065160930628980769756859931990,43376379741515098647985425804924879601418733263383850422598111312577593386358487364224325263259858969597179251430700334177085086070671449464377616596274930686913256608398943997830334161922260743497953638415364436460427838759705357463553196755185148779782007128058722284120672980828831033776489898432828082361,89884656743115797203643969326208167354925714643588468712364745929920911611342304769134404976757706776492814888985130026442956403037161947081508067139935189302454456558696954436501574072984903785582353419756739807211841909524953510682258535758101581242581094790592743585216465460932752002047977201839275936987,935386979343325361212450472438835748446251696899)
        if DSA.Verify(data, sig_str, key):
            print("true")
            return data
        else:
            return False
        


    # Read bytes from the file
    def readFile(self, file):
        fin = open(file, "r+")
        text = fin.read()
        fin.close()
        return text

    #Write bytes to a file
    def writeFile(self, file, text):
        fout = open(file, "w+")
        fout.write(text)
        fout.close()
        return
