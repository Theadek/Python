from random import randrange
#//jednorazowe tworzenie czlowieka w kostruktorze
#//makeOrganizm w losuj()
class Swiat:

    def __init__(self, rozmiar, logger):
        self.__wysokosc=rozmiar[1]
        self.__szerokosc=rozmiar[0]
        self.__plansza=[[None for y in range(self.__wysokosc)] for x in range(self.__szerokosc)]
        self._skillIsActive=False
        self._cooldown=0
        self._duration=0
        self._organizmy=[]
        self._logger=logger
        self.losuj(2)


    def wypiszPlansze(self):
        for i in self.__plansza:
            print(i)

    def getPlansza(self):
        return self.__plansza

    #to nie będzie potrzebne, było do testowania
    def setPlansza(self, x,y,val):
        self.__plansza[x][y]=val
        self.__plansza[self._x][self._y]=None

    def losuj(self, n):
        randX=0
        randY=0
        randC=0
        znak=None
        liczba_stworzen=11*n
        while liczba_stworzen > 0:
            randC=randrange(11)

            Gatunki=('A','B','C','Z','G','J','L','M','O','T','W')
            for g in Gatunki:
               for i in range(n):
                    znak=g
                    #if randC == 0: znak='A'
                    #elif randC == 1: znak='Z'
                    #elif randC == 2: znak='B'
                    #elif randC == 3: znak='G'
                    #elif randC == 4: znak='J'
                    #elif randC == 5: znak='L'
                    #elif randC == 6: znak='M'
                    #elif randC == 7: znak='O'
                    #elif randC == 8: znak='T'
                    #elif randC == 9: znak='W'
                    #elif randC == 10: znak='C'
                    while True:
                        randX=randrange(self.__szerokosc)
                        randY=randrange(self.__wysokosc)
                        if self.__plansza[randX][randY]==None:
                            #dodaj organizm
                            self.__plansza[randX][randY]=znak
                            liczba_stworzen-=1
                            break






