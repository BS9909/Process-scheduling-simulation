class Averages():
    '''
    Klasa odpowiedzialna za policzenie odpowiednich srednich, dla czasu oczekiwania i przetwarzania. 
    Dzieki niej nie trzeba w kazdej z klas liczacych srednia dla danych czasow, pisac tych samych metod, wystraczy 
    uzyc metody instancji tej klasy, ktora jest tworzona z jednoczesna inicjalizacja tablic zawierajacych potrzebne dane.
    '''
    def __init__(self, arr,wt,pt):
        '''
        Konstruktor klasy przyjmuje 4 argumenty, odpowiednio: self ktory zwraca instancje klasy na rzecz ktorej wywolywany jest dana metoda, arr 
        czyli zmienna ktora jest tablica przechowujaca czasy jakie procesy potrzebuja od procesora na wykonanie sie, wt czyli znowu dwuwymiaorwa tablica numpy
        przechowujaca czasy oczekiwania procecso, pt czyli tablica dwuwymiarowa numpy przechowujaca czasy przetwarzania procesow.
        '''
        self.arr=arr
        self.pt=pt
        self.wt=wt


    def waitingAverage(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda.
        Funkcja liczby sredni czas oczekiwania dla kazdego ciagu a nastepnie usrednia wszystkie 100 czasoow.
        Funkcja zwraca usrednione srednie czasy oczekiwania
        '''
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
        return round((s/100),2)
    
    def processingAverage(self):
        '''
        Funkcja przyjmuje jeden argument ktory jest refeencja do instancji klasy na rzecz ktorej wywolywana jest metoda.
        Funkcja liczby sredni czas przetwarzania dla kazdego ciagu a nastepnie usrednia wszystkie 100 czasoow.
        Funkcja zwraca usrednione srednie czasy przetwarzania
        '''
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
        return round((s/100),2)

