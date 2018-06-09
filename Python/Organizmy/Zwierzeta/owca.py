from swiat import *
from organizm import *
from zwierze import *

class Owca(Zwierze):

    def __init__(self, r):
        super(Owca, self).__init__(r)
        self._sila = 4;
        self._inicjatywa = 4;
        self._symbol = 'O';
        self._justBorn = true;
        self._alive = true;