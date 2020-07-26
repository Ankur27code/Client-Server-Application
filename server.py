#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:35:53 2020

@author: ankuraggarwal
"""

import socket
import pickle
import os
Header = 10
PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
file="/data.txt"
path=os.getcwd()+file
d = {}
data1=""

with open(path) as file:
    for line in file:
#        print(line)
        h=line.count("|")
        if h == 0 :
            line = "|"+line
        line =line.strip()  
        f = line.split("|")
        f[1] = f[1].replace(" ", "")
        if f[1] == "" or  f[1].isdigit():
            if h == 3 :
                while len(f) < 4:
                    f.append("")            
    #        print(f)
                if f[0] != "" : 
                    f[0] = f[0].upper()
                    d[f[0]] = f[0:]



    
    
def decode(data2):
    dd = data2
    dd = dd.split("|")
    data3=dd[0]  
#    print(data3)
    return data3


        
def formatw(d):
    f=[]
    for v in d.values():
       f=v
    return(f)
    

    

connect = True    
while connect:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established.")
    while connect:
        data = clientsocket.recv(1024)
        if data.decode("utf-8") != "9":
            data2 = data.decode("utf-8")
            data1 = decode(data2)
#            print("2"+data1)
            dd = data2.split("|")
#            data1=dd[0]
        if data1 == "7":
            p=list(d.values())
            p.sort(key = lambda x: x[0])
            mymsg = pickle.dumps(p)
            mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
            clientsocket.send(mymsg)
#            for values in d:
#                fd = "---Record----"
#                clientsocket.send(fd.encode("utf-8"))
#                for i in values:
#                    clientsocket.send(values[i].encode("utf-8"))
        if data1 == "2" :
            if dd[1] in d or dd[1] == "":
                m=" Customer already exists OR VALUE ENTERED MUST CONTAIN NAME "
            else:
                
                d[dd[1]] = [dd[1],dd[2],dd[3],dd[4]]
                m = "customer has been added !!!!"
            mymsg = pickle.dumps(m)
            mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
            clientsocket.send(mymsg)            
            
            
            
        if data1 == "1" or data1 == "3":
            if dd[1] not in d :
                m = "customer not found !!!!!!"
                mymsg = pickle.dumps(m)
                mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
                clientsocket.send(mymsg)
            else :
                if data1 == "1":
                    name = dd[1]
                    m = d[name]
                    mymsg = pickle.dumps(m)
                    mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
                    clientsocket.send(mymsg)  
                if data1 == "3":
                    name = dd[1]
                    del d[name]
                    m = " customer record deleted !!!!"
                    mymsg = pickle.dumps(m)
                    mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
                    clientsocket.send(mymsg) 
                    
                    
        if data1 == "8" :
                m = "----------- Good Bye ----------------"
#                mymsg = pickle.dumps(m)
#                mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
                clientsocket.send(m.encode("utf-8"))
                

                
                
        if data1 == "4" or data1 == "5" or data1 == "6":
            if dd[1] not in d :
                m = "customer not found !!!!!!"
                mymsg = pickle.dumps(m)
                mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
                clientsocket.send(mymsg)
            else :
                if data1 == "4":
                    name = dd[1]
                    d[name][1]=dd[2]
                    m = "customer record updated !!!!"
                    mymsg = pickle.dumps(m)
                    mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
                    clientsocket.send(mymsg)  
                if data1 == "5":
                    name = dd[1]
                    d[name][2]=dd[2]
                    m = "customer record updated !!!!"
                    mymsg = pickle.dumps(m)
                    mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
                    clientsocket.send(mymsg)
                if data1 == "6":
                    name = dd[1]
                    d[name][3]=dd[2]
                    m = "customer record updated !!!!"
                    mymsg = pickle.dumps(m)
                    mymsg=bytes(f'{len(mymsg):<{Header}}',"utf-8")+mymsg
                    clientsocket.send(mymsg)


                    
        
        if not data or data.decode("utf-8")== "end":
            print(f"Connection from {address} has been ended.")
            break
#        print(data)
#        msg = "ankur"
##        msg = bytes(f"{len(msg):<10}", 'utf-8')+msg
#        print(msg)
#        try:
#            clientsocket.send(msg.encode("utf-8"))
#        except:
#            print("exited")
    clientsocket.close()
server.close()