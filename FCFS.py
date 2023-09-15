from scipy.io.arff import loadarff
import math
import random
totaldata=[]
dataset=loadarff(open('ThyroidData.arff','r'))

table=[[float(a) for a in dataset[0][i]]for i in range(len(dataset[0]))]
#print(table)
hameyesatrha=[i for i in range(0,1034)]
satrjadid=[]
satrjadid=random.sample(hameyesatrha,len(hameyesatrha))
tdata=[] # data train
tdata1=[]
tdata2=[]
tdata3=[]
tdata4=[]
tdata5=[]
testdata1=[]
testdata2=[]
testdata3=[]
testdata4=[]
testdata5=[]
indtdata1=[]
indtdata2=[]
indtdata3=[]
indtdata4=[]
indtdata5=[]
indtestdata1=[]
indtestdata2=[]
indtestdata3=[]
indtestdata4=[]
indtdatadata5=[]
indtestdata1 = satrjadid[0:207]
indtdata1=satrjadid[207:]
indtestdata2 = satrjadid[207:414]
indtdata2=satrjadid[0:207]+satrjadid[414:]
indtestdata3 = satrjadid[414:621]
indtdata3=satrjadid[0:414]+satrjadid[621:]   
indtestdata4=satrjadid[620:827]
indtdata4=satrjadid[0:620]+satrjadid[827:]
indtestdata5=satrjadid[827:]
indtdata5=satrjadid[0:827]

  
#######################
def train(indx):
    tdata=[]
    for i in indx:
        tdata.append(table[i])
    return tdata
def test(indx):
    testdata=[] #data test
    for i in indx:
        testdata.append(table[i])
    return testdata
#difnum = fasele nominal
tdata1=train(indtdata1)
tdata2=train(indtdata2)
tdata3=train(indtdata3)
tdata4=train(indtdata4)
tdata5=train(indtdata5)
testdata1=test(indtestdata1)
testdata2=test(indtestdata2)
testdata3=test(indtestdata3)
testdata4=test(indtestdata4)
testdata5=test(indtestdata5)
print(len(tdata1))
#difnum = fasele nominal
teta=[]
for i in range(0,20):
    teta.append(0.1)
def z(teta , x):
    sumi = teta[0]
    for i in range(0,len(x)-1):
        sumi = sumi + teta[i+1]*(x[i])
    return sumi
#teta =[1,2,1]
#x = [1,1,4.5]
def g(Z):
    gz= 1/(1+ math.pow(math.e, float(-Z)))
    return gz
def update(alfa, teta , tdata , yasi):
    gi=[]
    for i in range(0,len(tdata)):
        gi.append(g(z(teta,tdata[i])))
#    error=[]
    before = []
    after = []
    for i in range(0,len(teta)):
        sumi =0
        before.append(teta[i])
        for j in range(0 , len(tdata)):
            if yasi == 1 :
                y = tdata[j][19]
                if y == 1:
                    y = 1
                else:
                    y = 0
            if yasi == 2 :
                y = tdata[j][19]
                if y == 2:
                    y = 1
                else:
                    y = 0
            if yasi == 3 :
                y = tdata[j][19]
                if y == 3:
                    y = 1
                else:
                    y = 0
            #print(tdata[j][i])
            if(i==0):
                sumi = sumi + ((gi[j] - y ) *1)   
            else:
                sumi = sumi + ((gi[j] - y ) *float(tdata[j][i]) )           
        #e = sumi/(len(tdata))
        #error.append(e)
        sss= teta[i] - ((alfa*sumi)/len(tdata))
        after.append(sss)
    rs = 0
    for l in range(0,len(after)):
        rs += after[l] - teta[l]
    #result.append(rs)
    tupl=(rs,after)
    return tupl
#teta=[0.5,0.5,0.5]
#tdata=[[0,1,b'1'],[2,5,b'2'],[3,2,b'3'],[-2,0,b'1'],[3,2,b'2']]
def converge(alfa , yasi , tdata , teta , difr):
    flag=True
    c=0
    while flag==True:
        c= c+1
#        print(c)
#        flagerror=True
        tupl=update(alfa,teta,tdata,yasi)
        #print(tupl)
        error=tupl[0]
        teta=tupl[1]
#        print(error)
        if(c%300==0):
            print(error)
        if abs(error)<difr:
            print(c)
            flag=False
            return teta
#print(converge(0.1 , 1 , tdata , teta , 0.001))                      
#update(0.1,teta,tdata,1)
def maximum (teta,data,alfa,difr,teta1,teta2,teta3):
#    teta1=converge(alfa , 1 , tdata , teta , difr)
#    teta2=converge(alfa , 2 , tdata , teta , difr)
#    teta3=converge(alfa , 3 , tdata , teta , difr)
    h1=g(z(teta1,data))
    h2=g(z(teta2,data))
    h3=g(z(teta3,data))
    maxh=max(h1,h2,h3)
    if maxh==h1:
        return(1)
    elif maxh==h2:
        return(2)
    elif maxh==h3:
        return(3)
def error(dataset,alfa,difr,teta,tdata):
    e=0
    mahsa=[]
    teta1=converge(alfa , 1 , tdata , teta , difr)
    teta2=converge(alfa , 2 , tdata , teta , difr)
    teta3=converge(alfa , 3 , tdata , teta , difr)
    for i in range (0, len(dataset)):
        mahsa = dataset[i]
        predict=maximum(teta,mahsa,alfa,difr,teta1,teta2,teta3)
        if predict!=mahsa[len(mahsa)-1]:
            e=e+1
    e1=(100*e)/len(dataset)
    return e1
sumtrain=0
sumtrain += error(tdata1,0.1,0.001,teta,tdata1)
sumtrain += error(tdata2,0.1,0.001,teta,tdata2)
sumtrain += error(tdata3,0.1,0.001,teta,tdata3)
sumtrain += error(tdata4,0.1,0.001,teta,tdata4)
sumtrain += error(tdata5,0.1,0.001,teta,tdata5)
print("error train = " + str(sumtrain/5))
sumtest=0
"""sumtest +=error(testdata1,0.1,0.001,teta,tdata1)
sumtest +=error(testdata2,0.1,0.001,teta,tdata2)
sumtest +=error(testdata3,0.1,0.001,teta,tdata3)
sumtest +=error(testdata4,0.1,0.001,teta,tdata4)
sumtest +=error(testdata5,0.1,0.001,teta,tdata5) 
print("error test = " + str(sumtest/5) )  """   
#a1=0
#a2=0


    
