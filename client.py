#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:17:53 2020

@author: ankuraggarwal
"""

import socket
import pickle
PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
Header=10
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
def choices() :
    print("Python DB Menu")
    print("\t")
    print("1. Find Customer")
    print("2. Add Customer")
    print("3. Delete Customer")
    print("4. Update age")
    print("5. Update address")
    print("6. Update phone")
    print("7. Print report")
    print("8. Exit")
    print("\t")
choices()
d =input("Select : ")
d=str(d)
print("\t")

def empty_try(msg):
    try:
        y=input(msg)
        y = y.replace(" ", "")
        return y
    except SyntaxError:
        y = None
        k =" "
        return k
        
def passes(value):
    try:
        value = int(value)
        value =str(value)
        return (value)
    except :
        print("enter valid age or space to not give any value :")
        k = input()
        return (k)
#        fgh= input("enter valid age write again")
#        passes(fgh)
        
def checkd(d):
    if d == "1" or d == "3"  :
        msg = "Enter Customer name  : "
        name = empty_try(msg)
        name = name.upper()
#        print("Enter Customer name :-")
#        name = input()
        st = d+"|"+ name
        return st
    if d == "2" :
        msg = "Enter Customer name : "
        name = empty_try(msg)   
        name = name.upper()
#        name = input("Enter Customer name : ")
        msg = "Enter Customer's value to age : "
        ss = empty_try(msg)
        if ss != "":
            ss = passes(ss)
            
#            
#        age= input("Enter Customer's value to age and to skip type 500: ")
#        ver_age = passes(age)
        msg = "Enter Customer's value to address : "
        address = empty_try(msg)
#        address= input("Enter Customer's value to address : ")
        msg = "Enter Customer's value to phone : "
        phone = empty_try(msg)
#        phone= input("Enter Customer's value to phone : ")
#        print("Enter Customer name and value to update in this format (name|age|address|phone) :-")
#        values = input()
        st = d+"|"+name+"|"+ss+"|"+address+"|"+phone
        return st
        
    if d == "4" or d == "5" or d == "6" :
#       print("Enter Customer name and value to update in this format (name|updated value) :-")
        msg = "Enter Customer name : "
        name = empty_try(msg)
        name = name.upper()
#        name = input("Enter Customer name : ")
        msg = "Enter Customer's value to update : "
        update_val= empty_try(msg)
#        update_val= input("Enter Customer's value to update : ")
        if d == "4" and d != "" :
          update_val = passes(update_val)
        st = d+"|"+name+"|"+update_val
        return st
    if d == "8":
        d = int(d)
        print("") 
        print("--------- good bye --------------")
        print("")
        print("")
        print("")
        print("")
         
        
        return d
        
    if d == "7":
#        print(d)        
        return d
    else:
        print("Wrong input Please choose between 1 to 8 and re-run the program:")
        d = input()
#        d = str(d)
        checkd(d)
    
         
    
try :
    connect = True
    while connect:
        complete_info =b''
        rec_msg =True
        d=checkd(d)
#        print(d)
        if d == "8":
            client.send(d.encode("utf-8"))
            mymsg = client.recv(1024).decode("utf-8")
            print(mymsg)
            
            connect =False
            break
        client.send(d.encode("utf-8"))
        if d == 8:
            connect =False
        while d != "8":
            
            while connect:
            
                mymsg = client.recv(16)
                if rec_msg:
                    x=int(mymsg[:Header])
                    rec_msg=False     
                complete_info += mymsg
                if len(complete_info)-Header == x:
                    m = pickle.loads(complete_info[Header:])
                    
                    if d == "7":
                        print ("")
                        print ("")
                        print ("------- REPORT FORMAT-------- ")
                        print (" NAME | AGE | ADDRESS | PHONE    ")
                        print ("----------------------------- ")
                        print ("")
                        print ("")
                        for s in m:
                             print(s[0] + "|" + s[1]+ "|" + s[2]+ "|" + s[3])
                             print ("")
                             
                        print ("")
                        print ("")
                        print ("----------------------------- ")
                        print ("         REPORT ENDED         ")
                        print ("----------------------------- ")
                        print ("")
                    else :
                        print(m)
                    rec_msg =True
                    complete_info =b''
                    if d == "8" :
                        client.shutdown()
                        break
                    print("\t")
                    choices()
                    d=input("Select :  ")
                    d=checkd(d)
                    client.send(d.encode("utf-8"))
    #            if more.lower() != 'Exit':
    #                d=input()
    #            else:
    #                break
except ValueError:
    
    print("exit")

client.close()
        
        
    
