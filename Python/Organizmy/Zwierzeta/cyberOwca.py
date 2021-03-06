from Organizmy.zwierze import Zwierze
from random import randrange

class CyberOwca(Zwierze):

    def __init__(self, r):
        super(CyberOwca, self).__init__(r)
        self._sila = 11
        self._inicjatywa = 4
        self._symbol = 'C'
        self._justBorn = True
        self._alive = True
        self._najblizszy_barszcz=None

    def szukajBarszczu(self):
        shortest_path = 100000
        for x in range(0, self._ref.getWidth()):
            for y in range(0, self._ref.getHeight()):
                if self._ref.getOrganizmAtXY(x, y) !=None:
                    if self._ref.getOrganizmAtXY(x,y).getSymbol()=='B':
                        if self._najblizszy_barszcz == None:
                            shortest_path = abs(self._x - x) + abs(self._y - y)
                            self._najblizszy_barszcz = (x, y)
                        elif abs(self._x - x) + abs(self._y - y) < shortest_path:
                            shortest_path = abs(self._x - x) + abs(self._y - y)
                            self._najblizszy_barszcz = (x, y)

    def akcja(self):
        if self._ref._licznik_barszczu>0:
        #if ret>0:
            self.szukajBarszczu()

            #idź w stronę barszczu
            print("Ilość barszczu: "+str(self._ref._licznik_barszczu))
            tmpX=self._x
            tmpY=self._y
            print(str(self._najblizszy_barszcz)+" "+str(self._x)+" "+str(self._y))

            #if self._najblizszy_barszcz[0] < self._x: tmpX-=1
            #elif self._najblizszy_barszcz[0] > self._x: tmpX+=1
            #elif self._najblizszy_barszcz[1] < self._y: tmpY-=1
            #elif self._najblizszy_barszcz[1] > self._y: tmpY+=1
            rand=randrange(2)
            if rand==0:
                if self._najblizszy_barszcz[1] == self._y:
                    if self._najblizszy_barszcz[0] < self._x: tmpX -= 1
                    elif self._najblizszy_barszcz[0] > self._x: tmpX+=1
                else:
                    if self._najblizszy_barszcz[1] < self._y: tmpY -= 1
                    elif self._najblizszy_barszcz[1] > self._y: tmpY += 1
            else:
                if self._najblizszy_barszcz[0] == self._x:
                    if self._najblizszy_barszcz[1] < self._y: tmpY -= 1
                    elif self._najblizszy_barszcz[1] > self._y: tmpY += 1
                else:
                    if self._najblizszy_barszcz[0] < self._x: tmpX -= 1
                    elif self._najblizszy_barszcz[0] > self._x: tmpX += 1
            print(str(tmpX-self._x)+" "+str(tmpY-self._y))
            if self._ref.getOrganizmAtXY(tmpX, tmpY) == None:
                self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
            else:
                self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y)

        else:
            super().akcja()


