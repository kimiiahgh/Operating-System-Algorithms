#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:14:07 2018

@author: apple
"""

from collections import deque
q_r=deque([]);
rr=[]         
index=[]          
name=[]
arv_t=[]
serv_t=[]
begin_t=[]
end_t=[]
wait_t=[]
total_t=[]
TotalServ=[]  
l=1000
t=0  
counter=0     
n=int(input("ENTER NUMBER OF PROCESSES :"))
q=float(input("ENTER THE AMOUNT OF q"))
name.append(input("ENTER THE NAME OF PROCESS :"))
arv_t.append(int(input("ENTER ARIVAL TIME OF THE PROCESS :")))
serv_t.append(int(input("ENTER THE SERVICE TIME OF THE PROCESS :")))


for i in range(1,n):
    name.append(input("ENTER THE NAME OF PROCESS :"))
    arv_t.append(int(input("ENTER ARIVAL TIME OF THE PROCESS :")))
    serv_t.append(int(input("ENTER THE SERVICE TIME OF THE PROCESS :")))
     
cl=0    
bool1=False   
while bool1==False:
    for i in range(0,n):
        if cl==arv_t[i]:
            rr.append((serv_t[i],name[i]))
            index.append(i)
            counter=counter+1
            
    if counter!=0:
        while counter!=0:
            """if rr[j]>q:
                rr[j]=rr[j]-q
            else:
                rr.remove(rr[j])"""
            for b in rr:
                if b>q:
                    b=b-q
                else:
                    rr.remove(b)
                
            counter=counter-1
print(end_t)            
            
              
        
        
               
