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

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080               # Arbitrary non-privileged 
PATH = "userlist.txt"

userlist = {}
connlist = {}

def conn_thread(conn, addr):
    global userlist
    global connlist
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
            #print(recv_tmp)
            pkt = BytesToPkt(recv_tmp)
            name = pkt.src
            passwd = pkt.data
        except socket.error:
            conn.close()
            return
        if pkt.typ == TYP_REG:
            if name in userlist:
                conn.sendall(PktToBytes(Packet(TYP_ERR, b'server', name, b'Username exists!')))
            else:
                userlist[name] = passwd
                writeUserData(name, passwd)
                conn.sendall(PktToBytes(Packet(TYP_ACK, b'server', name, b'Register successfully!')))
        elif pkt.typ == TYP_LOI:
            if name not in userlist:
                conn.sendall(PktToBytes(Packet(TYP_ERR, b'server', name, b'Username does not exist!')))
            elif userlist[name] != passwd:
                print(userlist[name])
                conn.sendall(PktToBytes(Packet(TYP_ERR, b'server', name, b'Password error!')))
            else:
                if name in connlist:
                    conn_tmp = connlist.pop(name)
                    try:
                        conn_tmp.sendall(PktToBytes(Packet(TYP_LOO, b'server', name, b'Account login at another place!')))
                        conn_tmp.close()
                    except socket.error:
                        return
                connlist[name] = conn
                conn.sendall(PktToBytes(Packet(TYP_ACK, b'server', name, b'Login successfully!')))
                break
    conn.setblocking(False)
    while True:
        try:
            recv_tmp = conn.recv(PKT_MAX_SIZE)
            if not recv_tmp:
                conn.close()
                return
            pkt = BytesToPkt(recv_tmp)
            if pkt.typ == TYP_LOO:
                connlist.pop(pkt.src)
                conn.close()
                break
            else:
                if pkt.dest not in connlist:
                    conn.sendall(PktToBytes(Packet(TYP_ERR, b'server', name, b'Destination user is not online!')))
                else:
                    connlist[pkt.dest].sendall(recv_tmp)
        except socket.error:
            pass
    return


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

