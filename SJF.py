import numpy as np
from Averages import *
from FCFS import *

class SJF:
    '''
        Klasa odpoweidzialna za policzenie czasu oczekiwania (metoda waitingTime) i czasu przetwarzania
        (metoda processing time) dla algorytmu SJF
    '''
    def __init__(self,arr,wt,pt):
        '''
        Konstruktor klasy przyjmuje 4 argumenty, odpowiednio: self ktory zwraca instancje klasy na rzecz ktorej wywolywany jest dana metoda, arr 
        czyli zmienna ktora jest tablica przechowujaca czasy jakie procesy potrzebuja od procesora na wykonanie sie, wt czyli znowu dwuwymiaorwa tablica numpy
        przechowujaca czasy oczekiwania procecso, pt czyli tablica dwuwymiarowa numpy przechowujaca czasy przetwarzania procesow
        '''
        self.arr = arr
        self.wt=wt
        self.pt=pt


    def shedule(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja odpoweidzialna za uszeregowanie w kolejnosci rosnacej czasow ktore procesy potrzebuja na dostep do procesora. 
        '''
        self.arr = self.arr.astype('int32') #O szeregowanie tablicy numpy musialem zapytac na forum StackOverflow.
        self.arr.sort(axis=1)
        #print(self.arr)
        return 
        
    #Gdy juz uporzadkujemy rosnaco czas procesora jaki kazdy proces potrzebuje
    #to algorytm SJF niewywlaszczajacy sprwadza sie wtedy do FCFS
    #tak wiec do obliczenia waitingTime i processingTime wykorzystalem kompozycje
    #i obiekt FCFS ktoremu przekazalem pusta tablice wt,pt i posrotowana tablice arr
    def waitingTime(self): 
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja oblicza czas oczekiwania poslugujac sie obiektem klasy FCFS. 
        '''
        fcfs = FCFS(self.arr,self.wt,self.pt)
        fcfs.waitingTime()
        return

    def processingTime(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja oblicza czas przetwarzania poslugujac sie obiektem klasy FCFS. 
        '''
        fcfs = FCFS(self.arr,self.wt,self.pt)
        fcfs.processingTime()
        return

    def averageProcessing(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja oblicza usredniony czas srednich czasow oczekiwania, wykorzystywany jest do tego obiekt klacy Averages
        Funkcja zwraca usredniony czas srednich czasu przetwarzaia
        '''
        averages = Averages(self.arr,self.wt,self.pt)  
        return averages.processingAverage()

    def averageWaiting(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda
        Funkcja oblicza usredniony czas srednich czasow przetwarzania, wykorzystywany jest do tego obiekt klacy Averages
        Funkcja zwraca usredniony czas srednich czasu oczekiwnaia
        '''        
        averages = Averages(self.arr,self.wt,self.pt)  
        return averages.waitingAverage()