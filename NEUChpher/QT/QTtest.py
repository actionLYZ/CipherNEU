from PyQt5 import QtWidgets,QtCore  
import Login

if __name__=="__main__":    
    import sys    
    
    app=QtWidgets.QApplication(sys.argv)

    #声明窗口
    loginWindow = Login.LoginWindow()
    
    loginWindow.show()          #打开登陆窗口   
    sys.exit(app.exec_()) 