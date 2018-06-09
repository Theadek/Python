from swiat import *
from organizm import *
from zwierze import *

class Wilk(Zwierze):

    def __init__(self, r):
        super(Wilk, self).__init__(r)
        self._sila = 9;
        self._inicjatywa = 5;
        self._symbol = 'W';
        self._justBorn = true;
        self._alive = true;