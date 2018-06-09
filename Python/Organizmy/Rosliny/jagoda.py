#from swiat import Swiat
from Organizmy.roslina import Roslina

class Jagoda(Roslina):
    def __init__(self, ref):
        super().__init__(ref)
        self._sila=99
        self._inicjatywa=0
        self._symbol='J'
        self._justBorn=True
        self._alive=True


    def kolizja(self, comingX, comingY):
        if self._ref.getOrganizmAtXY(comingX,comingY).getSila()>=self._sila:
            self._ref._logger.dodajLog(self._ref.fullname(self._ref.getOrganizmAtXY(comingX, comingY).getSymbol()) + " " +
                               str(comingX) + " " + str(comingY) +" ZJADA WILCZA JAGODE NA " + str(self._x) + " "+ str(self._y))
            self._ref.zabij(self)

        self._ref._logger.dodajLog(self._ref.fullname(self._ref.getOrganizmAtXY(comingX, comingY).getSymbol()) + " " +
                           str(comingX) + " " + str(comingY) + " GINIE OD WILCZEJ JAGODY NA " + str(self._x) + " " + str(self._y))
        self._ref.zabij(self._ref.getOrganizmAtXY(comingX, comingY))

