import os
from socket import *
import _thread as th
def sendit():
    while True:
        data=bytes(input(),'utf-8')
        send.sendto(data,('192.168.1.7',13003))
def receive():
    while True:
        print('\nhe: '+str(rec.recvfrom(1024)[0])[2:-1])
send=socket(AF_INET,SOCK_DGRAM)
rec=socket(AF_INET,SOCK_DGRAM)
rec.bind(('',13001))
th.start_new_thread(receive,())
sendit()
rec.close()
send.close()
os._exit(0)


