from Organizmy.organizm import Organizm
import random

class Zwierze(Organizm):

    def __init__(self, r):
        super(Zwierze, self).__init__(r)

    def akcja(self):
        tmpX = self._x
        tmpY = self._y
        posibilities = []
        posibilities = self._ref.availableMoves(self._x, self._y)
        kierunek = random.randrange(0, len(posibilities))
        if posibilities[kierunek] == "UP": tmpY+=1
        elif posibilities[kierunek] == "DOWN": tmpY+=1
        elif posibilities[kierunek] == "LEFT": tmpX-=1
        elif posibilities[kierunek] == "RIGHT": tmpX+=1

        if self._ref.getOrganizmAtXY(tmpX, tmpY) == None:
            self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
        else:
            self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y)

    def kolizja(self, comingX, comingY):
        if self._ref.getOrganizmAtXY(comingX, comingY).getSymbol() == self._symbol: # rozmnazanie
            posibilities = []
            posibilities = self._ref.availableMoves(self._x, self._y)

            while len(posibilities) > 0:

                tmpX = self._x
                tmpY = self._y
                kierunek = random.randrange(0, len(posibilities))
                if posibilities[kierunek] == "UP": tmpY-=1
                elif posibilities[kierunek] == "DOWN": tmpY+=1
                elif posibilities[kierunek] == "LEFT": tmpX-=1
                elif posibilities[kierunek] == "RIGHT": tmpX+=1

                if self._ref.getOrganizmAtXY(tmpX, tmpY) == None:
                    self._ref.makeOrganizm(tmpX, tmpY, self._symbol)
                    break
                else:
                    posibilities.remove(kierunek)

        elif self._ref.getOrganizmAtXY(comingX, comingY).getSila() >= self._sila:
            self._ref.moveOrganizm(comingX, comingY, self._x, self._y)
        else:
            self._ref._logger.dodajLog(ref.fullname(self._ref.getOrganizmAtXY(self._x, self._y).getSymbol()) + " " + self._x + " " + self._y +" ZABIJA " + self._ref.fullname_R(self._ref.getOrganizmAtXY(comingX, comingY).getSymbol()) + " " + comingX + " " + comingY)
            self._ref.removeOrganizm(comingX, comingY)


