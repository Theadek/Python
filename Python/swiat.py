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
                    while True:
                        randX=randrange(self.__szerokosc)
                        randY=randrange(self.__wysokosc)
                        if self.__plansza[randX][randY]==None:
                            #dodaj organizm
                            self.makeOrganizm(randX, randY,znak)
                            #self.__plansza[randX][randY]=znak
                            liczba_stworzen-=1
                            break

    def fullname(self, x):
        if x=='A': return "ANTYLOPA"
        elif x=='B': return "BARSZCZ"
        elif x=='C': return "CYBER-OWCA"
        elif x=='@': return "CZLOWIEK"
        elif x=='G': return "GUARANA"
        elif x=='J': return "JAGODA"
        elif x=='L': return "LIS"
        elif x=='M': return "MLECZ"
        elif x=='O': return "OWCA"
        elif x=='T': return "TRAWA"
        elif x=='W': return "WILK"
        elif x=='Z': return "ZOLW"

    def getSkill(self):
        return self._skillIsActive

    def getHeight(self):
        return self.__wysokosc

    def getWidth(self):
        return self.__szerokosc

    def availableMove(self, x,y):
        odp=[]
        if x!=0: odp.append("LEFT")
        if x!=self.__szerokosc-1: odp.append("RIGHT")
        if y!=0: odp.append("UP")
        if y!=self.__wysokosc-1: odp.append("DOWN")
        return odp

    def getOrganizmAtXY(self,x,y):
        return self.__plansza[x][y]

    def moveOrganizm(self, oldX, oldY, newX, newY):
        if self.__plansza[newX][newY]!=None:
            self._logger.dodajLog(
                self.fullname(self.__plansza[oldX][oldY]).getSymbol()+" z "+
                +"("+str(oldX)+","+str(oldY)+") zabija "+
                self.fullname(self.__plansza[newX][newY]).getSymbol() + " na " +
                +"(" + str(newX) + "," + str(newY) + ")"
            )
            self.__plansza[newX][newY].setAlive(False)

        self.__plansza[oldX][oldY].setX(newX)
        self.__plansza[oldX][oldY].setY(newY)
        self.__plansza[newX][newY]= self.__plansza[oldX][oldY]
        self.__plansza[oldX][oldY]=None


    def makeOrganizm(self, x, y, c):
        self._logger.dodajLog("Nowy organizm typu "+self.fullname(c)+
                              " na ("+str(x)+","+str(y)+")")

        if c=='W': self.__plansza[x][y]=Wilk(self)
        elif c=='O': self.__plansza[x][y]=Owca(self)
        elif c=='A': self.__plansza[x][y]=Antylopa(self)
        elif c=='Z': self.__plansza[x][y]=Zolw(self)
        elif c=='L': self.__plansza[x][y]=Lis(self)
        elif c=='C': self.__plansza[x][y]=CyberOwca(self)
        elif c=='T': self.__plansza[x][y]=Trawa(self)
        elif c=='B': self.__plansza[x][y]=Barszcz(self)
        elif c=='J': self.__plansza[x][y]=WilczaJagoda(self)
        elif c=='G': self.__plansza[x][y]=Guarana(self)
        elif c=='M': self.__plansza[x][y]=Mlecz(self)
        elif c=='@': self.__plansza[x][y]=Czlowiek(self)

        self.__plansza[x][y].setX(x)
        self.__plansza[x][y].setY(y)
        for o in range(0,len(self._organizmy)):
            if self.__plansza[x][y].getInicjatywa()>self._organizmy[o].getInicjatywa():
                self._organizmy.insert(o, self.__plansza[x][y])
                break
            elif o==len(self._organizmy)-1:
                self._organizmy.append(self.__plansza[x][y])
                break




