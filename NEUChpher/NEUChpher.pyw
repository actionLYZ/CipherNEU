from PyQt5 import QtWidgets,QtCore  
import QT.Chat
import QT.Login
import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8080
username = b""

if __name__=="__main__":  
    app=QtWidgets.QApplication(sys.argv)
    loginedChatWindows = QT.LoginedChat.LoginedChatWindow()
    chatWindows = QT.Chat.ChatWindows(loginedChatWindows)
    chatWindows.show()
    sys.exit(app.exec_())
