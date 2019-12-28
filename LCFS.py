import numpy as np
from Averages import *

class LCFS:
    def __init__(self,arr,wt,pt):
        #print("LCFS object created")
        self.arr = arr
        self.wt=wt
        self.pt=pt
        self.revArr=np.fliplr(self.arr)
    
    def waintingTime(self): #jest to czas oczekiwania dlatego ostatnie elemty wiersz musza byc uciete gdyz czas ich trwania nie wplywa na czas oczekiwania!!wiec range do 100 jest ok bo 100 nie jest zaliczane
        for i in range(0,100):
            self.wt[0,i]=0
        for i in range(0,100):
            for j in range(1,100):
                a=self.revArr[i,j-1]
                b=self.wt[i,j-1]
                self.wt[i,j] = int(a) + int(b)
        #print(self.wt)
        return 
        
    def processingTime(self):
        for i in range(0,100):
            for j in range(0,100):
                a=self.revArr[i,j]
                b=self.pt[i,j-1]
                self.pt[i,j] = int(a) + int(b)
        #print(self.pt)
        return
        
    def averageProcessing(self):
      averages = Averages(self.revArr,self.wt,self.pt)  
      return averages.processingAverage()

    def averageWaiting(self):
        averages = Averages(self.revArr,self.wt,self.pt)  
        return averages.waitingAverage()