from swiat import *
from organizm import *
from zwierze import *

class Lis(Zwierze):

    def akcja(self):
        posibilities = []
        posibilities = ref.availableMoves(self._x, self._y)
        tmpX = self._x, tmpY = self._y
        while len(posibilities) > 0:
            kierunek = random.randrange(0, len(posibilites))
            if posibilities[kierunek] == "UP":
                tmpY += 1
            elif posibilities[kierunek] == "DOWN":
                tmpY += 1
            elif posibilities[kierunek] == "LEFT":
                tmpX -= 1
            elif posibilities[kierunek] == "RIGHT":
                tmpX += 1

            if ref.getOrganizmAtXY(tmpX, tmpY) == null:
                ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
                break
            elif ((ref.getOrganizmAtXY(tmpX, tmpY).getSila() <= sila) or (ref.getOrganizmAtXY(tmpX, tmpY).getSymbol() == symbol)):
                ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y)
                break
            else:
                posibilities.pop(kierunek);

    def __init__(self, r):
        super(Lis, self).__init__(r)
        self._sila = 3;
        self._inicjatywa = 7;
        self._symbol = 'L';
        self._justBorn = true;
        self._alive = true;