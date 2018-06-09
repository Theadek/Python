
#//jednorazowe tworzenie czlowieka w kostruktorze
class Swiat:

    def __init__(self, rozmiar, logger):
        self.__wysokosc=rozmiar[1]
        self.__szerokosc=rozmiar[0]
        self.__plansza=[[None for y in range(self.__wysokosc)] for x in range(self.__szerokosc)]
        self._skillIsActive=False
        self._cooldown=0
        self._duration=0
        self.wypiszPlansze()
        self._organizmy=[]
        self._logger=logger


    def wypiszPlansze(self):
        for i in self.__plansza:
            print(i)

    def getPlansza(self):
        return self.__plansza

    #to nie będzie potrzebne, było do testowania
    def setPlansza(self, x,y,val):
        self.__plansza[x][y]=val
        self.__plansza[self._x][self._y]=None

    def losuj(self, liczba_stworzen):
        randX=0
        randY=0
        randC=0
        znak=None
        while liczba_stworzen > 0:
            do
                


