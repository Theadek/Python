#from swiat import Swiat
from Organizmy.roslina import Roslina

class Mlecz(Roslina):
    def __init__(self, ref):
        super().__init__(ref)
        self._sila=0
        self._inicjatywa=0
        self._symbol='M'
        self._justBorn=True
        self._alive=True


    def akcja(self):
        super().akcja()
        super().akcja()
        super().akcja()
