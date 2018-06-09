from swiat import *
import abc
class Organizm:

    def __init__(self, r):
        self._ref=r
        self._sila=None
        self._inicjatywa=None
        self._x=None
        self._y=None
        self._symbol=None
        self._justBorn=None
        self._alive=None
        self._ref=r

    def getSila(self):
        return self._sila

    def getInicjatywa(self):
        return self._inicjatywa

    def setX(self, x):
        self._x=x

    def setY(self, y):
        self._y=y

    def setSila(self, s):
        self._sila=s

    def getSymbol(self):
        return self._symbol

    def getBorn(self):
        return self._justBorn

    def getAlive(self):
        return self._alive

    def setBorn(self, b):
        self._justBorn=b

    def setAlive(self,a ):
        self._alive=a

    @abc.abstractmethod
    def akcja(self):
        pass

    @abc.abstractmethod
    def kolizja(self, comingX, comingY):
        pass

