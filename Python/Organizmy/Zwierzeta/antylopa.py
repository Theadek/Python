from Organizmy.zwierze import Zwierze
import random

class Antylopa(Zwierze):

    def akcja(self):
        i=0
        while  i < 2 :
            posibilities = []
            posibilities = self._ref.availableMoves(self._x, self._y);
            tmpX = self._x
            tmpY = self._y;
            kierunek = random.randrange(len(posibilities))
            szansa = random.randrange(2)
            if (posibilities[kierunek] == "UP"): tmpY-=1
            elif (posibilities[kierunek] == "DOWN"): tmpY+=1
            elif (posibilities[kierunek] == "LEFT"): tmpX-=1
            elif (posibilities[kierunek] == "RIGHT"): tmpX+=1
            if self._ref.getOrganizmAtXY(tmpX, tmpY) == None:
                self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
                i+=1
            elif (self._ref.getOrganizmAtXY(tmpX, tmpY).getSymbol() == self._symbol):
                self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y)
                break
            elif ((szansa == 1) and (self._ref.getOrganizmAtXY(tmpX, tmpY).getSila() > self._sila)):
                self.ucieczka()
                break
            else:
                self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y)
                break

    def ucieczka(self):
        posibilities = self._ref.availableMoves(self._x, self._y)
        while (len(posibilities) > 0):
            tmpX = self._x
            tmpY = self._y
            kierunek = random.randrange(len(posibilities))
            if (posibilities[kierunek] == "UP"): tmpY-=1
            elif (posibilities[kierunek] == "DOWN"): tmpY+=1
            elif (posibilities[kierunek] == "LEFT"): tmpX-=1
            elif (posibilities[kierunek] == "RIGHT"): tmpX+=1
            if (self._ref.getOrganizmAtXY(tmpX, tmpY) == None):
                self._ref._logger.dodajLog("ANTYLOPA UCIEKLA Z POLA " + str(self._x) + " " + str(self._y))
                self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
                break
            else:
                posibilities.pop(kierunek)

    def kolizja (self, comingX, comingY):
        if (self._ref.getOrganizmAtXY(comingX, comingY).getSymbol() == self._symbol):
            super().kolizja(comingX, comingY)
        else:
            szansa = random.randrange(2)
            if ((szansa == 1) and (self._ref.getOrganizmAtXY(comingX, comingY).getSila() >= self._sila)):
                self.ucieczka()
            else:
                super().kolizja(comingX, comingY)







    def __init__(self, r):
        super(Antylopa, self).__init__(r)
        self._sila = 4
        self._inicjatywa = 4
        self._symbol = 'A'
        self._justBorn = True
        self._alive = True