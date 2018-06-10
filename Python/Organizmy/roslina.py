from Organizmy.organizm import Organizm
from random import randrange

class Roslina(Organizm):

    def __init__(self, ref):
        super().__init__(ref)
        self._luck = 80

    def akcja(self):
        mozliwosci=self._ref.availableMoves(self._x,self._y)
        kierunek=None
        tmpX=None
        tmpY=None
        szansza=None

        while len(mozliwosci)>0:
            szansa=randrange(0,100)
            if szansa < self._luck:
                break
            tmpX, tmpY=self._x, self._y
            kierunek=randrange(len(mozliwosci))
            if mozliwosci[kierunek]=="UP": tmpY-=1
            elif mozliwosci[kierunek]=="DOWN": tmpY+=1
            elif mozliwosci[kierunek]=="LEFT": tmpX-=1
            elif mozliwosci[kierunek]=="RIGHT": tmpX+=1

            if self._ref.getOrganizmAtXY(tmpX, tmpY)==None:
                self._ref.makeOrganizm(tmpX, tmpY, self._symbol)
                break
            else:
                del(mozliwosci[kierunek])

    def kolizja(self,comingX, comingY):
        self._ref.moveOrganizm(comingX, comingY, self._x, self._y)
