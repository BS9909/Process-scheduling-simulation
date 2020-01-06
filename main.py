from FCFS import *
from LCFS import *
from SJF import *
from RoundRobin import *
import numpy as np
import os
import sys
np.set_printoptions(threshold=sys.maxsize)

arrayData = []
arr = np.empty((100,100), dtype=object)#array z wartosciami z pliku 100x100
wt = np.empty((100,100), dtype=object) #waiting time
pt = np.empty((100,100), dtype=object) #processing time

def getData(inputFile):
    if os.path.isfile(inputFile):
        column=0
        row=0
        #print("file exist")
        with open(inputFile) as data:
            for line in data:
                if row > 99:
                    row=0
                    column+=1
                arr[column,row] = line.strip()
                wt[column,row] = 0
                pt[column, row] = 0
                row+=1
    else:
        print("file",inputFile,"doesn't exist")
    return 

def saveFile(outputFile, wTime, pTime,algName):
    string = "--------------------------------" + "\n" + algName + ":" + "\n" + "Average of averages in waiting time: " + str(wTime) + "\n" + "Average of averages in proessing time: " + str(pTime) + "\n"
    file = open(outputFile, 'a') #option a-do not overwrite file
    file.write(string)
    file.close
    return

def getFCFS():
    #FCFS: 
    getData('input.txt')
    fcfs = FCFS(arr,wt,pt)
    fcfs.waintingTime()
    fw=fcfs.averageWaiting()
    fcfs.processingTime()
    fp=fcfs.averageProcessing()
    saveFile('output.txt', fw, fp,"FCFS")
    return

def getLCFS():
    #LCFS
    getData('input.txt')
    lcfs = LCFS(arr,wt,pt)
    lcfs.waintingTime()
    fw=lcfs.averageWaiting()
    lcfs.processingTime()
    fp=lcfs.averageProcessing()
    saveFile('output.txt', fw, fp,"LCFS")    
    return

def getSJF():
    #SJF
    getData('input.txt')
    sjf = SJF(arr,wt,pt)
    sjf.shedule()
    sjf.waitingTime()
    fw=sjf.averageWaiting()
    sjf.processingTime()
    fp=sjf.averageProcessing()
    saveFile('output.txt', fw, fp,"SJF")
    return 

def getRoundRobinFCFS():
    #RoundRobin
    q=[0.5,1,1.5]
    getData('input.txt')
    roundRobin = RoundRobin(arr,wt,pt)
    for  i in range(0,len(q)):
        rrString="Round Robin FCFS with quantum = " + str(q[i])
        roundRobin.waitingTime(q[i])
        fw=roundRobin.averageWaiting()
        roundRobin.processingTime()
        fp=roundRobin.averageProcessing()
        saveFile('output.txt', fw, fp,rrString)
    return 

def getRoundRobinLCFS():
    #RoundRobin
    q=[0.5,1,1.5]
    getData('input.txt')
    revArr=np.fliplr(arr)
    roundRobin = RoundRobin(revArr,wt,pt)
    for  i in range(0,len(q)):
        rrString="Round Robin LCFS with quantum = " + str(q[i])
        roundRobin.waitingTime(q[i])
        fw=roundRobin.averageWaiting()
        roundRobin.processingTime()
        fp=roundRobin.averageProcessing()
        saveFile('output.txt', fw, fp,rrString)
    return 

getFCFS()
getLCFS()
getSJF()
getRoundRobinFCFS()
getRoundRobinLCFS()