#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:19:12 2018

@author: apple
"""

import heapq
q=[]
n=int(input("ENTER NUMBER OF PROCESS"))
arv_t=[]
begin_t=[]
serv_t=[]
end_t=[]
total_t=[]
wait_t=[]
process=[]
c=0
t=1000
for i in range(0,n):
    process.append(input("ENTER PROCESS :"))
    arv_t.append(int(input("ENTER ARIVAL TIME OF THE PROCESS :")))
    serv_t.append(int(input("ENTER SERVICE TIME OF THE PROCESS :")))
    begin_t.append(0)
    end_t.append(0)
    t=t+serv_t[i]
for cl in range(0,t):
    for i in range(0,n):
        if cl==arv_t[i]:
            c=c+1
            heapq.heappush(q,(serv_t[i],process[i]))      
    if c==0:
        cl=cl+0
    elif c>=1:
        heapq.heapify(q)
        mini=heapq.heappop(q)
        p1=mini[1]
        s=mini[0]
        index1=process.index(p1)
        begin_t[index1]=cl
        end_t[index1]=cl+s
        c=c-1
        for pro in range(cl,cl+s):
            for j in range(0,n):
                if pro==arv_t[j]:
                    heapq.heappush(q,(serv_t[j],process[j]))
                    c=c+1
    
               
print(end_t)
print(begin_t)                   
        
    
