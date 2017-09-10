from PyQt5 import QtWidgets,QtCore  
import QT.Chat

'''
if __name__=="__main__":    
    import sys    
    
    app=QtWidgets.QApplication(sys.argv)

    #声明窗口
    loginWindow = Login.LoginWindow()
    
    loginWindow.show()          #打开登陆窗口   
    sys.exit(app.exec_()) '''

if __name__=="__main__":  
    import sys
    app=QtWidgets.QApplication(sys.argv)
    chatWindows = QT.Chat.ChatWindows()
    chatWindows.show()          #打开聊天窗口
    sys.exit(app.exec_())