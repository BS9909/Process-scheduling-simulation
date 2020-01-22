import numpy as np
from Averages import *

class RoundRobin:
    '''
        Klasa odpoweidzialna za policzenie czasu oczekiwania (metoda waitingTime) i czasu przetwarzania
        (metoda processing time) dla algorytmu Round Robin
    '''
    def __init__(self,arr,wt,pt):
        '''
        Konstruktor klasy przyjmuje 4 argumenty, odpowiednio: self ktory zwraca instancje klasy na rzecz ktorej wywolywany jest dana metoda, arr 
        czyli zmienna ktora jest tablica przechowujaca czasy jakie procesy potrzebuja od procesora na wykonanie sie, wt czyli znowu dwuwymiaorwa tablica numpy
        przechowujaca czasy oczekiwania procecso, pt czyli tablica dwuwymiarowa numpy przechowujaca czasy przetwarzania procesow.
        '''
        #print("RoundRobin object created")
        self.arr = arr 
        self.wt=wt
        self.pt=pt
        #self.q=q
        self.arr = self.arr.astype('float32') #konwersja danych zawartych w tablicy z int na float by moc liczyc czas oczekiwania 
        self.pt = self.pt.astype('float32')   #i przetwarzania dla kwantow zmiennoprzecinkowych
        self.wt = self.wt.astype('float32')


    def waitingTime(self,q):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda oraz 
        argument q ktory jest kwantem czasu.
        Funkcja liczy czas oczekiwania dla zadanego kwantu 'q' przekazanego w argumencie
        '''
        
        tmpArr = np.copy(self.arr) #Zmienna przechowujaca dokladna kopie tablicy z czasami procesow
        tmpArr = tmpArr.astype('float32')
        for i in range(0,100):#petla zmieniajaca ciagi procesow
            t=0             #deklaracja zmiennej odpoweidzialnej za liczenie czasu
            while 1:        #Powdoduje ze algorymt bedzie liczyl czas oczekiwania az kazdemu procesowi zostanie przyznany procesor
                done = True #Zmienna done ustawiona pocztakowo na True, od niej zalezy czy funkcja while zostaine przerwana
                for j in range(0,100):#petla zmieniajaca procey w danym ciagu
                    if tmpArr[i,j]>0: # Jesli czas wykoania procesu jest wiekszy od 0 to procesowi nalezy przydzielic kwant casu procesora
                        done = False  #zmiana zmiennej na false (oznacza to ze wszystkie procesy sie jeszcze nie wykonaly)
                        if tmpArr[i,j]>q: #jesli czas ktory jest potrzebny procesowi jest wiekszy niz czas kwantu to odejmij kwant od czasu procesroa
                            t=t+q         #dodaj czas kwantu do zmiennej liczacej czas oczekiwania 
                            tmpArr[i,j] = tmpArr[i,j] - q
                        else:               #w przeciwnym wypadku wyzeruj czas procesora => proces zostal wykonany
                            t=t+tmpArr[i,j] #przypisz zmiennej liczacej czas oczekiwania czas jaki pozostal procesowi do wykonania
                            self.wt[i,j]=t-self.arr[i,j] #dodaj do tablicy zawierajacej czasy oczekiwania czas oczekiwania danego procesu
                            tmpArr[i,j]=0     #zakoncz proces
                if done == True:            #jesli wszystkie procesy zostana wykoanane to program nie wejdzie w warunek ktory zmieni zmienna done na false przez co petla while zostanie przerwana
                    break
        #print(self.wt)
        return
    
    def processingTime(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda oraz argument q ktory jest
        kwantem czasu
        Policzenie czasu przetwarzania to dodanie do czasu oczekiwania czas jaki proces potrzebuje na wykonanie
        '''
        for i in range(0,100):
            for j in range(0,100):
                self.pt[i,j]=self.wt[i,j] + self.arr[i,j]
        
        #print(self.pt)
        return

    def averageProcessing(self):
        '''
        Liczymy sredni czas przetwarzania za pomoca obiektu Average zawierajacego metody 
        potrzebne do policzenia odpoweidnich srednich
        Funkcja zwraca usredniony czas srednich czasu przetwarzania
        '''
        averages = Averages(self.arr,self.wt,self.pt)  
        return averages.processingAverage()

    def averageWaiting(self):
        '''
        Liczymy sredni czas oczekiwania za pomoca obiektu Average zawierajacego metody 
        potrzebne do policzenia odpoweidnich srednich
        Funkcja zwraca usredniony czas srednich czasu oczekiwnaia
        '''
        averages = Averages(self.arr,self.wt,self.pt)  
        return averages.waitingAverage()