from random import randrange
from Organizmy.organizm import Organizm
from Organizmy.roslina import Roslina
from Organizmy.Rosliny.mlecz import Mlecz
from Organizmy.Rosliny.trawa import Trawa
from Organizmy.Rosliny.guarana import Guarana
from Organizmy.Rosliny.jagoda import Jagoda
from Organizmy.Rosliny.barszcz import Barszcz
from Organizmy.Zwierzeta.wilk import Wilk
from Organizmy.Zwierzeta.owca import Owca
from Organizmy.Zwierzeta.lis import Lis
from Organizmy.Zwierzeta.zolw import Zolw
from Organizmy.Zwierzeta.antylopa import Antylopa
from Organizmy.Zwierzeta.czlowiek import Czlowiek
from Organizmy.Zwierzeta.cyberOwca import CyberOwca
from logger import Logger
import pickle


#//jednorazowe tworzenie czlowieka w kostruktorze
#//makeOrganizm w losuj()
#//dodać sprawdzzanie czy skill aktywny
class Swiat:

    def __init__(self, rozmiar, logger, okno):
        from oknoController import Okno
        self.__wysokosc=rozmiar[1]
        self.__szerokosc=rozmiar[0]
        self.__plansza=[[None for y in range(self.__wysokosc)] for x in range(self.__szerokosc)]
        self._skillIsActive=False
        self._cooldown=0
        self._duration=0
        self._licznik_barszczu=0
        self._organizmy=[]
        self._logger=logger
        #self._okno=okno
        self._klawisz=""
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


    def czysc(self):
        for o in self._organizmy:
            if o.getAlive()==False:
                self._organizmy.remove(o)

    def usun_wszystko(self):
        self._organizmy.clear()
        for x in range(self.__szerokosc):
            for y in range(self.__wysokosc):
                self.__plansza[x][y]=None

    def wykonajTure(self):
        if ((self._klawisz == 'q') and (self._cooldown == 0) and (self._skillIsActive == False)):
            self._skillIsActive = True
            self._duration = 5
            self._logger.dodajLog("UMIEJETNOSC CZLOWIEKA AKTYWOWANA")
        elif (self._klawisz == 'q'):
            if(self._skillIsActive == True):
                self._logger.dodajLog("UMIEJETNOSC JEST JUZ AKTYWNA")
            else:
                self._logger.dodajLog("UMIEJETNOSC MUSI SIE ODNOWIC")
        else:

            for o in self._organizmy:
                if o.getAlive()==False: pass
                elif o.getBorn()==True: o.setBorn(False)
                else: o.akcja()

            self.czysc()

            if ((self._skillIsActive) and (self._duration > 0)):
                self._duration-=1
            elif ((self._skillIsActive) and (self._duration == 0)):
                self._skillIsActive = False
                self._cooldown = 5
                self._logger.dodajLog("WYCZERPANIE UMIEJETNOSCI CZLOWIEKA")
            elif (self._cooldown > 0):
                self._cooldown-=1
                if (self._cooldown == 0):
                    self._logger.dodajLog("UMIEJETNOSC CZLOWIEKA ODNOWIONA")

    def losuj(self, n):
        randX=0
        randY=0
        randC=0
        znak=None
        self.makeOrganizm(0,0, "@")
        Gatunki=('A','B','C','Z','G','J','L','M','O','T','W')
        Gatunki=('B','C')
        for g in Gatunki:
            for i in range(n):
                znak=g
                while True:
                    randX=randrange(self.__szerokosc)
                    randY=randrange(self.__wysokosc)
                    if self.__plansza[randX][randY]==None:
                        #dodaj organizm
                        self.makeOrganizm(randX, randY,znak)
                        break
        self.wykonajTure()

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


    def fullname_R(self, x):
        if x == 'A': return "ANTYLOPE";
        elif x == 'B': return "BARSZCZ";
        elif x == 'C': return "CYBER-OWCE";
        elif x == '@': return "CZLOWIEKA"
        elif x == 'G': return "GUARANE";
        elif x == 'J': return "JAGODE";
        elif x == 'L': return "LISA";
        elif x == 'M': return "MLECZA";
        elif x == 'O': return "OWCE";
        elif x == 'T': return "TRAWE";
        elif x == 'W': return "WILKA";
        elif x == 'Z': return "ZOLWA";


    def getKlawisz(self):
        return self._klawisz

    def setKlawisz(self, klawisz):
        self._klawisz=klawisz

    def getSkill(self):
        return self._skillIsActive

    def getHeight(self):
        return self.__wysokosc

    def getWidth(self):
        return self.__szerokosc

    def availableMoves(self, x,y):
        odp=[]
        if x!=0: odp.append("LEFT")
        if x!=self.__szerokosc-1: odp.append("RIGHT")
        if y!=0: odp.append("UP")
        if y!=self.__wysokosc-1: odp.append("DOWN")
        return odp

    def getOrganizmAtXY(self,x,y):
        return self.__plansza[x][y]

    def zabij(self, org):
        self._organizmy.remove(self.getOrganizmAtXY(org.getX(), org.getY()))
        self.__plansza[org.getX()][org.getY()] = None

    def moveOrganizm(self, oldX, oldY, newX, newY):
        if self.__plansza[newX][newY]!=None:
            self._logger.dodajLog(
                self.fullname(self.__plansza[oldX][oldY].getSymbol())+" z "+
                "("+str(oldX)+","+str(oldY)+") zabija "+
                self.fullname(self.__plansza[newX][newY].getSymbol()) + " na "+
                "(" + str(newX) + "," + str(newY) + ")"
            )
            self.__plansza[newX][newY].setAlive(False)

        self.__plansza[oldX][oldY].setX(newX)
        self.__plansza[oldX][oldY].setY(newY)
        self.__plansza[newX][newY]= self.__plansza[oldX][oldY]
        self.__plansza[oldX][oldY]=None


    def makeOrganizm(self, x, y, c):
        print("wololo")
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
        elif c=='J': self.__plansza[x][y]=Jagoda(self)
        elif c=='G': self.__plansza[x][y]=Guarana(self)
        elif c=='M': self.__plansza[x][y]=Mlecz(self)
        elif c=='@': self.__plansza[x][y]=Czlowiek(self)

        #debugowanie
        #print(type(self.__plansza[x][y]))
        #print(str(x)+" "+str(y))
        #print(self.__plansza[x][y].getSymbol())
        self.__plansza[x][y].setX(x)
        self.__plansza[x][y].setY(y)
        if len(self._organizmy)==0:
            self._organizmy.append(self.__plansza[x][y])
        else:
            for o in range(0,len(self._organizmy)):
                if self.__plansza[x][y].getInicjatywa()>self._organizmy[o].getInicjatywa():
                    self._organizmy.insert(o, self.__plansza[x][y])
                    break
                elif o==len(self._organizmy)-1:
                    self._organizmy.append(self.__plansza[x][y])
                    break




