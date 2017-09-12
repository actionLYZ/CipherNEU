from PyQt5 import QtCore, QtGui, QtWidgets
from QT import Register,Setting, Chat, LoginedChat
import Resource.LogResource
import GlobalWindow


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(361, 185)
        Login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Login.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Login.setStyleSheet("selection-background-color: rgb(0, 0, 255);\n"
"selection-background-color: rgb(0, 0, 127);")
        self.layoutWidget = QtWidgets.QWidget(Login)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 162))
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
        self.lab_nickname = QtWidgets.QLabel(self.layoutWidget)
        self.lab_nickname.setObjectName("lab_nickname")
        self.horizontalLayout_4.addWidget(self.lab_nickname)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.line_nickname = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_nickname.setObjectName("line_nickname")
        self.horizontalLayout_4.addWidget(self.line_nickname)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.lab_password = QtWidgets.QLabel(self.layoutWidget)
        self.lab_password.setObjectName("lab_password")
        self.horizontalLayout_5.addWidget(self.lab_password)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.line_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_password.setObjectName("line_password")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_5.addWidget(self.line_password)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.but_setting = QtWidgets.QPushButton(self.layoutWidget)
        self.but_setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_setting.setObjectName("but_setting")
        self.horizontalLayout_6.addWidget(self.but_setting)
        self.but_login = QtWidgets.QPushButton(self.layoutWidget)
        self.but_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_login.setObjectName("but_login")
        self.horizontalLayout_6.addWidget(self.but_login)
        self.but_register = QtWidgets.QPushButton(self.layoutWidget)
        self.but_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_register.setObjectName("but_register")
        self.horizontalLayout_6.addWidget(self.but_register)
        self.but_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.but_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_cancel.setObjectName("but_cancel")
        self.horizontalLayout_6.addWidget(self.but_cancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.b = QtWidgets.QListWidget(Login)
        self.b.setGeometry(QtCore.QRect(-5, -9, 371, 201))
        self.b.setStyleSheet("border-image: url(:/images/background.png);")
        self.b.setObjectName("background")
        self.b.raise_()
        self.layoutWidget.raise_()
        
        self.retranslateUi(Login)
        self.but_cancel.clicked.connect(Login.close)
        self.but_setting.clicked.connect(self.OpenSetting)
        self.but_register.clicked.connect(self.OpenRegister)
        self.but_login.clicked.connect(self.IfLogin)
        QtCore.QMetaObject.connectSlotsByName(Login)

    #判断用户是否允许登陆
    def IfLogin(self):
        if self.line_nickname.text() == "" or self.line_password.text() == "":
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","用户名或密码不能为空！",QtWidgets.QMessageBox.Yes)

        elif not self.line_nickname.text().isalnum() and self.line_password.text().isalnum():
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","用户名和密码必须由字母与数字组成！",QtWidgets.QMessageBox.Yes)
            ifpass = False

        else:
            ifLoginRight = self.IfLoginRight()

    #输入的用户名密码是否正确
    def IfLoginRight(self):
        document = open("User.txt","r")
        for context in document.readlines():
            if self.line_nickname.text() == context[:context.find(' ')]:
                if self.line_password.text() == context[context.find(' ')+1:-1]:
                    message = QtWidgets.QMessageBox()
                    message.about(self,"Pass","登陆成功！")
                    message.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    document.close()
                    
                    GlobalWindow.globalWindow.logedwindow.label_4.setText("Welcome!\n\n" + self.line_nickname.text())
                    GlobalWindow.globalWindow.logedwindow.show()
                    GlobalWindow.globalWindow.chatwindow.close()
                    
                    return True

                else:
                    message = QtWidgets.QMessageBox()
                    message.warning(self,"Error","用户名与密码不匹配！",QtWidgets.QMessageBox.Ok)
                    document.close()
                    return False

        message = QtWidgets.QMessageBox()
        message.warning(self,"Error","用户名不存在！",QtWidgets.QMessageBox.Ok)
        document.close()
        return False

    def OpenRegister(self):
        self.registerWindow = Register.RegisterWindow()
        self.registerWindow.show()

    def OpenSetting(self):
        self.settingWindow = Setting.SettingWindow()
        self.settingWindow.show()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.lab_nickname.setText(_translate("Login", "Nickname"))
        self.lab_password.setText(_translate("Login", "Password"))
        self.but_setting.setText(_translate("Login", "Setting"))
        self.but_login.setText(_translate("Login", "Login"))
        self.but_register.setText(_translate("Login", "Register"))
        self.but_cancel.setText(_translate("Login", "Cancel"))



#登陆窗口对象
class LoginWindow(QtWidgets.QWidget,Ui_Login):  
    def __init__(self):    
        super(LoginWindow,self).__init__()  
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint )        #只允许最小和关闭，不允许最大化,不允许调整大小
        self.setupUi(self)
