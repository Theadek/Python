from oknoController import Okno
from swiat import Swiat
from random import randint
from logger import Logger
from Organizmy import organizm

log=Logger()
okno = Okno(log,(20,20))
#wczytywanie rozmiaru, na razie na sztywno ustawiam 20 x 20
#rozmiar=okno.wczytaj_rozmiar()
rozmiar=(20,20)
#rozmiar jest tuplą, ma w sobie (szerokość, wysokość)
swiat=Swiat(rozmiar)
okno.setSwiat(swiat)

#org=Organizm(swiat)

okno.symulacja()

