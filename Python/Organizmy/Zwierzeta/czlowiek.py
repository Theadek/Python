from Organizmy.zwierze import Zwierze
import random

class Czlowiek(Zwierze):

    def akcja(self):

        zn=self._ref.getKlawisz()
        tmpX = self._x
        tmpY = self._y
        if ((zn == "up") and (self._y != 0)):
            tmpY -=1
            if(self._ref.getOrganizmAtXY(tmpX, tmpY) == None): self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
            elif (self._ref.getOrganizmAtXY(tmpX, tmpY).getSila() <= self._sila): self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y)
            elif (self._ref.getSkill()): self._ucieczka()
            else: self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y)
            
        elif ((zn == "down") and (self._y != self._ref.getHeight() - 1)):
            tmpY+=1
            if (self._ref.getOrganizmAtXY(tmpX, tmpY) == None): self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
            elif (self._ref.getOrganizmAtXY(tmpX, tmpY).getSila() <= self._sila): self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y);
            elif (self._ref.getSkill()): self._ucieczka()
            else: self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y);
            
        elif ((zn == "left") and (self._x != 0)):
            tmpX-=1
            if (self._ref.getOrganizmAtXY(tmpX, tmpY) == None): self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
            elif (self._ref.getOrganizmAtXY(tmpX, tmpY).getSila() <= self._sila): self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y);
            elif (self._ref.getSkill()): self._ucieczka()
            else: self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y);
            
        elif ((zn == "right") and (self._x != self._ref.getWidth() - 1)):
            tmpX+=1
            if (self._ref.getOrganizmAtXY(tmpX, tmpY) == None): self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
            elif (self._ref.getOrganizmAtXY(tmpX, tmpY).getSila() <= self._sila): self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y);
            elif (self._ref.getSkill()): self._ucieczka()
            else: self._ref.getOrganizmAtXY(tmpX, tmpY).kolizja(self._x, self._y);

    

    def kolizja(self, comingX, comingY):
        if ((self._ref.getSkill() == False) or (self._ref.getOrganizmAtXY(comingX, comingY).getSila() < self._sila)):
            super().kolizja(comingX, comingY)
        else:
            self._ucieczka()


    def _ucieczka(self):
        posibilities = []
        posibilities = self._ref.availableMoves(self._x, self._y)
        while (len(posibilities) > 0):
            tmpX = self._x
            tmpY = self._y
            kierunek = random.randrange(len(posibilities))
            if (posibilities[kierunek] == "UP"): tmpY-=1
            elif (posibilities[kierunek] == "DOWN"):tmpY+=1
            elif (posibilities[kierunek] == "LEFT"):tmpX-=1
            elif (posibilities[kierunek] == "RIGHT"):tmpX+=1

            if (self._ref.getOrganizmAtXY(tmpX, tmpY) == None):
                self._ref._logger.dodajLog("CZLOWIEK UCIEKL Z POLA " + str(self._x) +" " + str(self._y))
                self._ref.moveOrganizm(self._x, self._y, tmpX, tmpY)
                break
            else:
                posibilities.pop(kierunek)



    def __init__(self, r):
        super(Czlowiek, self).__init__(r)
        self._sila = 5
        self._inicjatywa = 4
        self._symbol = '@'
        self._justBorn = True
        self._alive = True