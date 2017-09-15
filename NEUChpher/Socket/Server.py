'''
Name: Socket - Server
Programmer: AI
Date: 2017-09-04
'''

'''
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080               # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
'''

# Echo server program
import socket
import _thread
from Packet import *
import os
from DH import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080               # Arbitrary non-privileged 
PATH = "userlist.txt"

userlist = {}
connlist = {}
p = 0
g = 0

def conn_thread(conn, addr):
    global userlist
    global connlist
    global p, g
    send_tmp = b''
    recv_tmp = b''
    name = b''
    passwd = b''
    while True:
        try:
            recv_tmp = conn.recv(PKT_MAX_SIZE)
            if not recv_tmp:
                conn.close()
                break
            pkt = BytesToPkt(recv_tmp)
            name = pkt.src
            passwd, sep, temp = pkt.data.partition(b"<<<<<<")
        except socket.error:
            conn.close()
            return
        if pkt.typ == TYP_REG:
            if name in userlist:
                conn.sendall(PktToBytes(Packet(TYP_ERR, b'server', name, b'Username exists!')))
                return
            else:
                userlist[name] = passwd
                writeUserData(name, passwd)
                conn.sendall(PktToBytes(Packet(TYP_ACK, b'server', name, b'Register successfully!')))
                return
        elif pkt.typ == TYP_LOI:
            if name not in userlist:
                conn.sendall(PktToBytes(Packet(TYP_ERR, b'server', name, b'Username does not exist!')))
                return
            elif userlist[name] != passwd:
                print(userlist[name])
                conn.sendall(PktToBytes(Packet(TYP_ERR, b'server', name, b'Password error!')))
                return
            else:
                if name in connlist:
                    conn_tmp = connlist.pop(name)
                    try:
                        conn_tmp.sendall(PktToBytes(Packet(TYP_LOO, b'server', name, b'Account login at another place!')))
                        conn_tmp.close()
                    except socket.error:
                        pass
                connlist[name] = conn
                conn.sendall(PktToBytes(Packet(TYP_ACK, b'server', name, b'Login successfully!')))
                p, g = generate()
                for user in connlist:
                    connlist[user].sendall(PktToBytes(Packet(TYP_KEY, b'server', user, str(p) + ">>>>>>" + str(g))))
                break
    conn.setblocking(False)
    while True:
        try:
            recv_tmp = conn.recv(PKT_MAX_SIZE)
            '''
            if not recv_tmp:
                conn.close()
                return
            '''
            if transmitPacket(recv_tmp, name) == False:
                return
        except socket.error:
            continue
        '''
        try:
            conn.sendall(send_tmp)
            send_tmp = b''
        except socket.error:
            pass
        '''
    return


def transmitPacket(bys, name):
    bys, sep, temp = bys.partition(b"<<<<<<")
    pkt = BytesToPkt(bys)
    if pkt.typ == TYP_LOO:
        connlist.pop(pkt.src)
        conn.close()
        return False
    elif pkt.typ == TYP_KEY:
        for user in connlist:
            if user != name:
                connlist[user].sendall(PktToBytes(Packet(TYP_KEY, name, user, pkt.data)))
    else:
        if pkt.dest not in connlist:
            conn.sendall(PktToBytes(Packet(TYP_ERR, b'server', name, b'Destination user is not online!')))
        else:
            connlist[pkt.dest].sendall(recv_tmp)
    return True

def readUserData():
    global userlist
    try:
        fin = open(PATH, "rb")
    except FileNotFoundError:
        fin = open(PATH, "wb")
        fin.close()
        return
    data = fin.readline()
    while (data):
        name, sep, passwd = data.partition(b' ')
        passwd, sep, temp = passwd.partition(b'\r\n')
        userlist[name] = passwd
        data = fin.readline()
    fin.close()
    return

def writeUserData(name, passwd):
    global userlist
    fin = open(PATH, "ab")
    fin.write(name + b' ' + passwd + b'\r\n')
    fin.close()
    return

def input_thread(temp):
    while True:
        temp = input()
        if temp == "exit":
            os._exit(0)
    return

readUserData()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    _thread.start_new_thread(input_thread, ("exit", ))
    while True:
        conn, addr = s.accept()
        _thread.start_new_thread(conn_thread, (conn, addr))
    s.close()

