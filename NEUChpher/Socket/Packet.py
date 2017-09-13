'''
Name: Socket - Packet
Programmer: AI
Date: 2017-09-04
'''
 
import re

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

PKT_MAX_SIZE = 4096
DOWNLOAD_PATH = "downloads/"

class Packet:
    def __init__(self, typ, src, dest, data):
        self.typ = typ
        self.src = src
        self.dest = dest
        self.data = data

class User:
    def __init__(self, name, passwd, conn):
        self.name = name
        self.passwd = passwd
        self.conn = conn

'''
type>>>>>>src>>>>>>dest>>>>>>data
'''

def PktToBytes(pkt):
    tmp = b''
    if isinstance(pkt.typ, str):
        tmp += pkt.typ.encode()
    else:
        tmp += pkt.typ
    tmp += b'>>>>>>'
    if isinstance(pkt.src, str):
        tmp += pkt.src.encode()
    else:
        tmp += pkt.src
    tmp += b'>>>>>>'
    if isinstance(pkt.dest, str):
        tmp += pkt.dest.encode()
    else:
        tmp += pkt.dest
    tmp += b'>>>>>>'
    if isinstance(pkt.data, str):
        tmp += pkt.data.encode()
    else:
        tmp += pkt.data
    return tmp

def BytesToPkt(tmp):
    sep = b'>>>>>>'
    typ, sep, tmp  = tmp.partition(b'>>>>>>')
    src, sep, tmp  = tmp.partition(b'>>>>>>')
    dest, sep, data  = tmp.partition(b'>>>>>>')
    return Packet(typ, src, dest, data)

def isValidIpv4Address(addr):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')  
    if p.match(addr):  
        return True  
    else:  
        return False 
