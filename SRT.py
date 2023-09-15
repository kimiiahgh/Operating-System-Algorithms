#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:02:20 2018

@author: apple
"""

import pygame
import heapq
name=[]
arv_t=[]
serv_t=[]
begin_t=[]
end_t=[]
wait_t=[]
l=[]
total_t=[]
TotalServ=[]
#q=heapq.heapify((rem_t,name))
q=[]
t=1000
pygame.init()
gameDisplay = pygame.display.set_mode((1000,1000))  
gameDisplay.fill((230,230,250))
heapq.heapify(q)

n=int(input("ENTER NUMBER OF PROCESSES :"))
name.append(input("ENTER THE NAME OF PROCESS :"))
arv_t.append(int(input("ENTER ARIVAL TIME OF THE PROCESS :")))
serv_t.append(int(input("ENTER THE SERVICE TIME OF THE PROCESS :")))
#q.heappush(serv_t[0],namel[0])
t=t+serv_t[0]
for i in range(1,n):
    name.append(input("ENTER THE NAME OF PROCESS :"))
    arv_t.append(int(input("ENTER ARIVAL TIME OF THE PROCESS :")))
    serv_t.append(int(input("ENTER THE SERVICE TIME OF THE PROCESS :")))
    t=t+serv_t[i]


counter=0 
x=0      
for cl in range(0,t):
    for i in range(0,n):
        if arv_t[i]==cl:
            heapq.heappush(q,(serv_t[i],name[i]))
            counter=counter+1
    if counter!=0:
         heapq.heapify(q)
         mini=heapq.heappop(q)
         pygame.draw.rect(gameDisplay,(171,130,255),[20+x,60,40,20])
         pygame.draw.rect(gameDisplay,(93,71,139),[20+x,60,40,20],3)
         x=x+40
         counter=counter-1
         d=mini[0]-1
         if d!=0:
             heapq.heappush(q,(d,mini[1]))
             counter=counter+1
         else:
             end_t.append((cl+1,mini[1]))
    else:
        pygame.draw.rect(gameDisplay,(230,230,250),[20+x,60,40,20])
        pygame.draw.rect(gameDisplay,(230,230,250),[20+x,60,40,20],3)
        x=x+40
pygame.display.update()         

for j in range(0,n):
    l.append(0)
for m in range(0,n):
    P=end_t[m][1]
    index=name.index(P)
    k=end_t[m][0]
    l[index]=k
print("PROCESS"," ","WAITING TIME"," ","TOTAL TIME","  ","Tt/Ts")     
for i in range(0,n):
    wait_t.append(l[i]-arv_t[i]-serv_t[i])
    total_t.append(wait_t[i]+serv_t[i])
    TotalServ.append(total_t[i]/serv_t[i])
    print("  ",name[i],"         ",wait_t[i],"         ",total_t[i],"      ",TotalServ[i])
    
    
    
   
     
     
  
    
    
    
            
        
"""    heapq.heapify(q)
    mini=heapq.heappop(q)
    if mini[0]==serv_t[i]:
        begin_t.append(cl)
    d=mini[0]
    if d!=0:
        heapq.heappush(q,(d,mini[1])) """
        
    
                           
"""   for i in range(0,r):
        minn=heapq.heappop(q)
        d=minn[0]
        if d!=0:
            heapq.heappush(q,(minn[0],minn[1]))
    heapq.heappush(q,(minn[0]-1,minn[1]))   """    
#check for ///// write wait & total time
        
            
            
        
            
        
    
    
   
    
    
       
    
    
        
         
