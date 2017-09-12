import socket
from Packet import *

def recvThread(sock):
    while True:
        try:
            recv_tmp = s.recv(PKT_MAX_SIZE)
            pkt = BytesToPkt(recv_tmp)
            if pkt.typ == TYP_PTX:
                print(pkt.src.decode() + ': ' + pkt.data.decode())
            elif pkt.typ == TYP_LOO:
                print('Error: ' + pkt.data.decode())
                s.close()
                os._exit(0)
            else:
                print(recv_tmp.decode())
        except socket.error:
            pass
    return