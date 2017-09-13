from PyQt5 import QtWidgets,QtCore  
from QT import Chat,Login,LoginedChat
import sys
import GlobalWindow

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    loginedWindows = LoginedChat.LoginedChatWindow()
    chatWindows = Chat.ChatWindows()
    loginWindow = Login.LoginWindow()
    GlobalWindow.globalWindow.setWindow(loginWindow,chatWindows,loginedWindows)
    GlobalWindow.globalWindow.chatwindow.show()
    sys.exit(app.exec_())
