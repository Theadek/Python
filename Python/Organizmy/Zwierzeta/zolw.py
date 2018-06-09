from Organizmy.zwierze import Zwierze
import random

class Zolw(Zwierze):

    def akcja(self):
        szansa = random.randrange(4);
        if szansa == 0: super().akcja();


    def kolizja(self, comingX, comingY):
        if ref.getOrganizmAtXY(comingX, comingY).getSymbol() == self._symbol:
            super().kolizja(comingX, comingY)
        elif ref.getOrganizmAtXY(comingX, comingY).getSila() >= 5:
            super().kolizja(comingX, comingY)
        else:
            ref.logger.dodajLog("ZOLW " + self._x + " " + self._y + " ODPARL PROBE ATAKU " + ref.fullname_R(ref.getOrganizmAtXY(comingX, comingY).getSymbol()) + " " + comingX + " " + comingY)

    def __init__(self, r):
        super(Zolw, self).__init__(r)
        self._sila = 2;
        self._inicjatywa = 1;
        self._symbol = 'Z';
        self._justBorn = True;
        self._alive = True;