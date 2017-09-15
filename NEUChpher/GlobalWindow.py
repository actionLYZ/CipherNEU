import socket

class MainWindow():
    def __init__(self):
        self.loginwindow=None
        self.logedwindow=None
        self.chatwindow=None
    def setWindow(self,loginwindow,chatwindow,logedwindow):
        self.loginwindow=loginwindow
        self.logedwindow=logedwindow
        self.chatwindow=chatwindow

globalWindow=MainWindow()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8080
username = b""
isFile = False
enCipherType = "None"
deCipherType = "None"
encryptKey = ""
decryptKey = ""

uploadPath = ""
downloadPath = ""

filetype = ""
filedata = ""
fileIsEncrypted = False

keylist = {}
key = 0
p = 0
g = 0

C1x = []
C1y = []
C2x = []
C2y = []
Add = []
str_len = 0
result = ""
ecc_ciphertext = ""
