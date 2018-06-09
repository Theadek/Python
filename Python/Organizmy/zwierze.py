from swiat import *
from organizm import *
import abc
import random

class Zwierze(Organizm):

    def __init__(self, r):
        super(Zwierze, self).__init__(r)

    def akcja(self):
        tmpX = self._x
        tmpY = self._y
        posibilites = []
        posibilites = ref.availableMoves(self._x, self._y)
        kierunek = random.randrange(0, len(posibilites))
        if posibilities[kierunek] == "UP": tmpY+=1
        elif posibilities[kierunek] == "DOWN": tmpY+=1
        elif posibilities[kierunek] == "LEFT": tmpX-=1
        elif posibilities[kierunek] == "RIGHT": tmpX+=1

        if ref.getOrganizmAtXY(tmpX, tmpY) == None:
            ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
        else:
            ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y)

    def kolizja(self, comingX, comingY):
        if ref.getOrganizmAtXY(comingX, comingY).getSymbol() == self._symbol: # rozmnazanie
            posibilities = []
            posibilities = ref.availableMoves(self._x, self._y)

            while len(posibilities) > 0:

                tmpX = self._x
                tmpY = self._y
                kierunek = random.randrange(0, len(posibilities))
                if posibilities[kierunek] == "UP": tmpY-=1
                elif posibilities[kierunek] == "DOWN": tmpY+=1
                elif posibilities[kierunek] == "LEFT": tmpX-=1
                elif posibilities[kierunek] == "RIGHT": tmpX+=1

                if ref.getOrganizmAtXY(tmpX, tmpY) == None:
                    ref.makeOrganizm(tmpX, tmpY, self._symbol)
                    break
                else:
                    posibilities.remove(kierunek)

        elif ref.getOrganizmAtXY(comingX, comingY).getSila() >= self._sila:
            ref.moveOrganizm(comingX, comingY, self._x, self._y)
        else:
            ref.logger.dodajLog(ref.fullname(ref.getOrganizmAtXY(self._x, self._y).getSymbol()) + " " + self._x + " " + self._y +" ZABIJA " + ref.fullname_R(ref.getOrganizmAtXY(comingX, comingY).getSymbol()) + " " + comingX + " " + comingY)
            ref.removeOrganizm(comingX, comingY)


