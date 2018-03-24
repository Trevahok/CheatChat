import os
from socket import *
udpsock=socket(AF_INET,SOCK_DGRAM)
rec=socket(AF_INET,SOCK_DGRAM)
rec.bind(('',13003))
while True:
    data=bytes(input('enter message to send: '),'utf-8')
    udpsock.sendto(data,('192.168.1.7',13003))
    print('received: '+str(rec.recvfrom(1024))[2:-1])
rec.close()
udpsock.close()
os._exit(0)
