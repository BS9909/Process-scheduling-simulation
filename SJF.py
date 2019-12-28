import numpy as np
from Averages import *
from FCFS import *

class SJF:
    def __init__(self,arr,wt,pt):
        #print("SJF object created")
        self.arr = arr
        self.wt=wt
        self.pt=pt

    def shedule(self):
        self.arr = self.arr.astype('int32')
        self.arr.sort(axis=1)
        #print(self.arr)
        return 
        
    #Gdy juz uporzadkujemy rosnaco czas procesora jaki kazdy proces potrzebuje
    #to algorytm SJF niewywlaszczajacy sprwadza sie wtedy do FCFS
    #tak wiec do obliczenia waitingTime i processingTime wykorzystalem kompozycje
    #i obiekt FCFS ktoremu przekazalem pusta tablice wt,pt i posrotowana tablice arr
    def waitingTime(self): 
        fcfs = FCFS(self.arr,self.wt,self.pt)
        fcfs.waintingTime()
        return

    def processingTime(self):
        fcfs = FCFS(self.arr,self.wt,self.pt)
        fcfs.processingTime()
        return

    def averageProcessing(self):
      averages = Averages(self.arr,self.wt,self.pt)  
      return averages.processingAverage()

    def averageWaiting(self):
        averages = Averages(self.arr,self.wt,self.pt)  
        return averages.waitingAverage()