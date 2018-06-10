#from swiat import Swiat
from Organizmy.roslina import Roslina
from Organizmy.zwierze import Zwierze

class Barszcz(Roslina):
    def __init__(self, ref):
        super().__init__(ref)
        self._sila=10
        self._inicjatywa=0
        self._symbol='B'
        self._justBorn=True
        self._alive=True


    def akcja(self):
        posibilities = []
        posibilities = self._ref.availableMoves(self._x, self._y)
        i = 0
        while i < len(posibilities) :
            tmpX = self._x
            tmpY = self._y
            if (posibilities[i] == "UP"): tmpY-=1
            elif (posibilities[i] == "DOWN"): tmpY+=1
            elif (posibilities[i] == "LEFT"): tmpX-=1
            elif (posibilities[i] == "RIGHT"): tmpX+=1

            if ((self._ref.getOrganizmAtXY(tmpX, tmpY) != None) and (isinstance(self._ref.getOrganizmAtXY(tmpX,tmpY), Zwierze))):
                if (self._ref.getOrganizmAtXY(tmpX, tmpY).getSymbol() == 'C'):
                    pass
                if ((self._ref.getOrganizmAtXY(tmpX, tmpY).getSymbol() != '@') or (self._ref.getSkill()==False)):
                    self._ref._logger.dodajLog("BARSZCZ Z " + str(self._x) + " " + str(self._y) + " ZABIJA " + self._ref.fullname_R(self._ref.getOrganizmAtXY(tmpX, tmpY).getSymbol()) + str(tmpX) + " " + str(tmpY))
                    self._ref.zabij(self._ref.getOrganizmAtXY(tmpX, tmpY))
                else:
                    self._ref._logger.dodajLog("CZLOWIEK Z " + str(tmpX) + " " + str(tmpY) + " UCHRONIL SIE OD ATAKU BARSZCZU")
            i+=1

        super().akcja()


    def kolizja(self, comingX, comingY):
        if(self._ref.getOrganizmAtXY(comingX,comingY).getSymbol() == 'C'):
            self._ref._logger.dodajLog(self._ref.fullname("CYBER-OWCA " + str(comingX) + " " + str(comingY) + " ZJADA CALY KRZAK BARSZCZU " + str(self._x) + " " + str(self._y)))
            self._ref.zabij(self)
            self._ref._licznik_barszczu = -1

        if (self._ref.getOrganizmAtXY(comingX, comingY).getSila() >= self._sila):
            self._ref._logger.dodajLog(self._ref.fullname(self._ref.getOrganizmAtXY(comingX, comingY).getSymbol()) + " " + str(comingX) + " " + str(comingY) +" ZJADA CALY KRZAK BARSZCZU " + str(self._x) + " " + str(self._y))
            self._ref.zabij(self)
            self._ref._licznik_barszczu=-1

        self._ref._logger.dodajLog(self._ref.fullname(self._ref.getOrganizmAtXY(comingX, comingY).getSymbol())+ " " + str(comingX) + " " + str(comingY) +" UMIERA OD BARSZCZU " + str(self._x) + " " + str(self._y))
        self._ref.zabij(self._ref.getOrganizmAtXY(comingX, comingY))