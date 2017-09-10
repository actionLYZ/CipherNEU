# File Name: Protocol.py
# Programmer(s): AI
# Last Modified Time: 2017-09-08 17:50
# Description: Self-difined communication protocol between two clients through the server.

'''
b'typ>>>>>>src>>>>>>dest>>>>>>data'
'''

# Imports

import socket

# Constants

TYP_REG = b'reg' # register
TYP_LOI = b'loi' # login
TYP_KEY = b'key' # public key
TYP_PTX = b'ptx' # plaintext
TYP_CTX = b'ctx' # ciphertext
TYP_PFL = b'pfl' # plain file
TYP_CFL = b'cfl' # cipher file
TYP_LOO = b'loo' # logout
TYP_ACK = b'ack' # acknowledgement
TYP_ERR = b'err' # error

PKT_MAX = 4096  #  maximum packet size

# Data Structures

class Packet:

    def __init__(self, typ, src, dest, data):
        self.typ = typ
        self.src = src
        self.dest = dest
        self.data = data

    def toBytes(self):
        tmp = b''
        if isinstance(self.typ, bytes):
            tmp += self.typ
        else:
            tmp += self.typ.encode()
        tmp += b'>>>>>>'
        if isinstance(self.src, bytes):
            tmp += self.src
        else:
            tmp += self.src.encode()
        tmp += b'>>>>>>'
        if isinstance(self.dest, bytes):
            tmp += self.dest
        else:
            tmp += self.dest.encode()
        tmp += b'>>>>>>'
        if isinstance(self.data, bytes):
            tmp += self.data
        else:
            tmp += self.data.encode()
        return tmp

# Algorithms & Functions

def toPacket(bys):
    sep = b'>>>'
    typ, sep, tmp  = tmp.partition(b'>>>>>>')
    src, sep, tmp  = tmp.partition(b'>>>>>>')
    dest, sep, data  = tmp.partition(b'>>>>>>')
    return Packet(typ, src, dest, data)

def isType(bys, typ):
    if toPacket(bys).typ == typ:
        return True
    else:
        return False

def send(s, typ, src, dest, text):
    try:
        s.sendall(Packet(typ, src, dest, text).toBytes())
        return True
    except socket.serror:
        return False

def receive(s):
    try:
        tmp = s.recv(PKT_MAX)
        if tmp:
            return toPacket(tmp)
    except socket.error:
        return None

def readFile(path):
    fin = open(path, 'rb')
    tmpa, sep, tmp = fin.name.encode().rpartition(b'\\')
    tmp += b'>>>>>>'
    tmp += fin.read()
    fin.close()
    return tmp

def writeFile(bys, path):
    name, sep, tmp = bys.partition(b'>>>>>>')
    fout = open(path + name, 'wb')
    fout.write(tmp)
    fout.close()
    return

'''
def receiveThread(sock):
    try:
        tmp = sock.recv(PKT_MAX)
        if tmp:

    except socket.error:
        pass
    return

def sendThread(name, sock):

    return
'''
