import numpy as np
from Averages import *

class LCFS:
    '''
    Klasa odpoweidzialna za policzenie czasu oczekiwania (metoda waitingTime) i czasu przetwarzania
    (metoda processing time) dla algorytmu LCFS
    '''
    def __init__(self,arr,wt,pt):
        '''
        Konstruktor klasy przyjmuje 4 argumenty, odpowiednio: self ktory zwraca instancje klasy na rzecz ktorej wywolywany jest dana metoda, arr 
        czyli zmienna ktora jest tablica przechowujaca czasy jakie procesy potrzebuja od procesora na wykonanie sie, wt czyli znowu dwuwymiaorwa tablica numpy
        przechowujaca czasy oczekiwania procecso, pt czyli tablica dwuwymiarowa numpy przechowujaca czasy przetwarzania procesow.
        '''
        self.arr = arr
        self.wt=wt
        self.pt=pt
        self.revArr=np.fliplr(self.arr) #obrocenie kolejnosci ciagow tablicy 

    
    def waintingTime(self): 
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja oblicza czas oczekiwania.
         '''
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
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja oblicza czas przetwarzania.
         '''
        for i in range(0,100):
            for j in range(0,100):
                a=self.revArr[i,j]
                b=self.pt[i,j-1]
                self.pt[i,j] = int(a) + int(b)
        #print(self.pt)
        return
        
    def averageProcessing(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja oblicza usredniony czas srednich czasow przetwarzania.
        Funkcja zwraca usredniony czas srednich czasu przetwarzania.
        '''
        averages = Averages(self.revArr,self.wt,self.pt)  
        return averages.processingAverage()

    def averageWaiting(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja oblicza usredniony czas srednich czasow oczekiwnia.
        Funkcja zwraca usredniony czas srednich czasu oczekiwnaia
        '''
        averages = Averages(self.revArr,self.wt,self.pt)  
        return averages.waitingAverage()