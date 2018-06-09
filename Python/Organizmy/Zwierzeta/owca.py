from Organizmy.zwierze import Zwierze
<<<<<<< HEAD
=======

>>>>>>> a6c42c0fc6da3ad6f491757526072113e462d7b0
class Owca(Zwierze):

    def __init__(self, r):
        super(Owca, self).__init__(r)
        self._sila = 4;
        self._inicjatywa = 4;
        self._symbol = 'O';
        self._justBorn = True;
        self._alive = True;