from oknoController import Okno
from swiat import Swiat
from random import randint
from logger import Logger
from random import randrange
from Organizmy import organizm

log=Logger()
okno = Okno(log,(15,15))
#wczytywanie rozmiaru, na razie na sztywno ustawiam 20 x 20
#rozmiar=okno.wczytaj_rozmiar()
rozmiar=(15,15)
#rozmiar jest tuplą, ma w sobie (szerokość, wysokość)
swiat=Swiat(rozmiar, log)
swiat.losuj(2)
okno.setSwiat(swiat)

#org=Organizm(swiat)

okno.symulacja()

