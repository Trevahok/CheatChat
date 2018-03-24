from socket import *
from tkinter import *
import os
import _thread as th
server=input('enter my creators ip: ')
port=13003
def _quit():
    rec.close()
    send.close()
    os._exit(0)
    main.destroy()
def addchat(event=None):
    dat=txt.get()
    send.sendto(bytes(dat,'utf-8'),(server,port))
    chist.insert(END,'\nYou: '+dat)
    txt.delete(0,END)

send=socket(AF_INET,SOCK_DGRAM)
rec=socket(AF_INET,SOCK_DGRAM)
rec.bind(('',port))

main=Tk()
main.bind('<Return>',addchat)

txt=Entry(main,bg='black',fg='white')
chist=Text(main,height=50,width=50,bg='black',fg='white')
quit=Button(main,text='Quit',command=_quit)
quit.pack(side=BOTTOM,fill=X)
txt.pack(side=BOTTOM,fill=X)
chist.pack(side=BOTTOM,fill=X)

def receive():
    while True:
        dat,ip=rec.recvfrom(1024)
        chist.insert(END,'\n'+str(dat)[2:-1])
        main.lift()
th.start_new_thread(receive,())
main.mainloop()

