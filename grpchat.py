from socket import *
from tkinter import *
import os
import _thread as th
ipname={}
ipbook=[]
myip='172.16.9.159'
port=13004
def _quit():
    rec.close()
    send.close()
    main.destroy()
    os._exit(0)
def addchat(event=None):
    dat=txt.get()
    for ip in ipbook:
        send.sendto(bytes(ip+': '+dat,'utf-8'),(ip,port))
    chist.insert(END,'\nYou: '+dat)
    txt.delete(0,END)

send=socket(AF_INET,SOCK_DGRAM)
rec=socket(AF_INET,SOCK_DGRAM)
rec.bind(('',port))

main=Tk()
main.title('CheatChat')
main.bind('<Return>',addchat)

txt=Entry(main,bg='black',fg='white')
chist=Text(main,height=50,width=50,bg='black',fg='white')
quit=Button(main,text='Quit',command=_quit,bg='black',fg='white')
quit.pack(side=BOTTOM,fill=X)
txt.pack(side=BOTTOM,fill=X)
chist.pack(side=BOTTOM,fill=X)

def receive():
    while True:
        main.lift()
        data,ipadd=rec.recvfrom(1024)
        chist.insert(END,'\n'+ipadd[0]+': '+str(data)[2:-1])
        if ipadd[0] not in ipbook:
            ipbook.append(ipadd[0])
        for ip in [i for i in ipbook if i!=ipadd[0]]:
            send.sendto(bytes(ipadd[0]+': '+str(data)[2:-1],'utf-8'),(ip,port))
th.start_new_thread(receive,())
main.mainloop()
