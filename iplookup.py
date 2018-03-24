from socket import *
from tkinter import *
import os
import _thread as th
ipbook={}
myip='Creator'
port=13003
def _quit():
    rec.close()
    send.close()
    main.destroy()
    os._exit(0)
def addchat(event=None):
    dat=txt.get()
    for ip in ipbook.keys():
        send.sendto(bytes(myip+': '+dat,'utf-8'),(ip,port))
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
        if ipadd[0] not in ipbook.keys():
            send.sendto(bytes('server: enter how you would like to be refered as: ','utf-8'),(ipadd[0],port))
            ipbook[ipadd[0]]=str(rec.recvfrom(1024)[0])[2:-1]
        chist.insert(END,'\n'+ipbook[ipadd[0]]+': '+str(data)[2:-1])
        for ip in [i for i in ipbook.keys() if i!=ipadd[0]]:
            send.sendto(bytes(ipbook[ipadd[0]]+': '+str(data)[2:-1],'utf-8'),(ip,port))
th.start_new_thread(receive,())
main.mainloop()
