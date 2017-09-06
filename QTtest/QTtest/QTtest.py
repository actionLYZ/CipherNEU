from PyQt5 import QtWidgets,QtCore  
from Login import Ui_Login
from register import Ui_register
from Setting import Ui_Setting
    
#登陆窗口对象
class LoginWindow(QtWidgets.QWidget,Ui_Login):  
    def __init__(self):    
        super(LoginWindow,self).__init__()  
        #self.setWindowFlags(QtCore.Qt.SplashScreen)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint )        #只允许最小和关闭，不允许最大化,不允许调整大小
        self.setupUi(self)  
  
#注册窗口对象
class RegisterWindow(QtWidgets.QWidget,Ui_register):  
    def __init__(self):    
        super(RegisterWindow,self).__init__()  
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint)        #只允许最小和关闭，不允许最大化,不允许调整大小
        self.setupUi(self)  

#设置窗口对象
class SettingWindow(QtWidgets.QWidget,Ui_Setting):  
    def __init__(self):    
        super(SettingWindow,self).__init__()  
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint)        #只允许最小和关闭，不允许最大化,不允许调整大小
        self.setupUi(self)  

if __name__=="__main__":    
    import sys    
    
    app=QtWidgets.QApplication(sys.argv)

    #声明窗口
    loginWindow = LoginWindow()
    registerWindow = RegisterWindow()
    settingWindow = SettingWindow()

    #给登陆窗口对象中的成员分配槽
    loginWindow.but_register.clicked.connect(registerWindow.show)
    loginWindow.but_setting.clicked.connect(settingWindow.show)
    

    loginWindow.show()          #打开登陆窗口   
    sys.exit(app.exec_()) 