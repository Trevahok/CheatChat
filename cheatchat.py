from socket import *
from tkinter import *
import os
import _thread as th
def _quit():
    rec.close()
    send.close()
    os._exit(0)
    main.destroy()
def addchat(event=None):
    dat=txt.get()
    send.sendto(bytes(dat,'utf-8'),('192.168.1.7',13003))
    chist.insert(END,'\nYou: '+dat)
    txt.delete(0,END)

send=socket(AF_INET,SOCK_DGRAM)
rec=socket(AF_INET,SOCK_DGRAM)
rec.bind(('',13001))

main=Tk()
main.bind('<Return>',addchat)

txt=Entry(main)
chist=Text(main,height=50,width=50)
quit=Button(main,text='Quit',command=_quit)
quit.pack(side=BOTTOM,fill=X)
txt.pack(side=BOTTOM,fill=X)
chist.pack(side=BOTTOM,fill=X)

def receive():
    while True:
        chist.insert(END,'\nHe: '+str(rec.recvfrom(1024)[0])[2:-1])
th.start_new_thread(receive,())
main.mainloop()
