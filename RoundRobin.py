import numpy as np
from Averages import *

class RoundRobin:
    def __init__(self,arr,wt,pt):
        #print("RoundRobin object created")
        self.arr = arr
        self.wt=wt
        self.pt=pt
        #self.q=q
        self.arr = self.arr.astype('float32')
        self.pt = self.pt.astype('float32')
        self.wt = self.wt.astype('float32')

    #liczenie czasu oczekiwania kazdego procesu, nasty-do poprawy rozbij na
    #poszczegolne funkcje na labach
    def waitingTime(self,q):
        tmpArr = np.copy(self.arr)
        for i in range(0,100):
            t=0
            while 1:
                done = True
                for j in range(0,100):
                    if tmpArr[i,j]>0:
                        done = False
                        if tmpArr[i,j]>q:
                            t=t+q
                            tmpArr[i,j] = tmpArr[i,j] - q
                        else:
                            t=t+tmpArr[i,j]
                            self.wt[i,j]=t-self.arr[i,j]
                            #print("t= ",t)
                            tmpArr[i,j]=0
                if done == True:
                    break
        #print(self.wt)
        return
    
    def processingTime(self):
        for i in range(0,100):
            for j in range(0,100):
                self.pt[i,j]=self.wt[i,j] + self.arr[i,j]
        
        #print(self.pt)
        return

    def averageProcessing(self):
      averages = Averages(self.arr,self.wt,self.pt)  
      return averages.processingAverage()

    def averageWaiting(self):
        averages = Averages(self.arr,self.wt,self.pt)  
        return averages.waitingAverage()