from Organizmy.zwierze import Zwierze
class Wilk(Zwierze):

    def __init__(self, r):
        super(Wilk, self).__init__(r)
        self._sila = 9;
        self._inicjatywa = 5;
        self._symbol = 'W';
        self._justBorn = True;
        self._alive = True;