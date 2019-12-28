class Averages():
    def __init__(self, arr,wt,pt):
        self.arr=arr
        self.pt=pt
        self.wt=wt

    def waitingAverage(self):
        arrAverage = []
        sum = [] 
        a=0
        s=0
        self.arr = self.arr.astype('int32')
        for i in range(0,100):
            for j in range(0,100):
                a=a+self.wt[i,j]
            sum.append(a)
            a=0
        for i in range(0,100):
            arrAverage.append(sum[i]/100)
              
        for i in range(0,100):
            s=arrAverage[i]+s
        return s/100
    
    def processingAverage(self):
        arrAverage = []
        sum = [] 
        a=0
        s=0
        self.arr = self.arr.astype('int32')
        for i in range(0,100):
            for j in range(0,100):
                a=a+self.pt[i,j]
            sum.append(a)
            a=0
        for i in range(0,100):
            arrAverage.append(sum[i]/100)
        for i in range(0,100):
            s=arrAverage[i]+s
        return s/100

