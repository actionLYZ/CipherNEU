from PyQt5 import QtWidgets,QtCore  
import QT.Chat
import QT.Login
import sys

if __name__=="__main__":  
    app=QtWidgets.QApplication(sys.argv)
    loginedChatWindows = QT.LoginedChat.LoginedChatWindow()
    chatWindows = QT.Chat.ChatWindows(loginedChatWindows)
    chatWindows.show()
    sys.exit(app.exec_())