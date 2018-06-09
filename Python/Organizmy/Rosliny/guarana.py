#from swiat import Swiat
from Organizmy.roslina import Roslina

class Guarana(Roslina):
    def __init__(self, ref):
        super().__init__(ref)
        self._sila=0
        self._inicjatywa=0
        self._symbol='G'
        self._justBorn=True
        self._alive=True


    def kolizja(self,comingX, comingY):
        print("Przed zjedzenie guarany: "+str(self._ref.getOrganizmAtXY(comingX, comingY).getSila()))
        self._ref.getOrganizmAtXY(comingX, comingY).setSila(self._ref.getOrganizmAtXY(comingX, comingY).getSila()+3)
        print("Po zjedzeni guarany: " + str(self._ref.getOrganizmAtXY(comingX, comingY).getSila()))
        self._ref.moveOrganizm(comingX, comingY, self._x, self._y)
