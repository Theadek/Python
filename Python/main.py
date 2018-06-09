from oknoController import Okno
from swiat import Swiat
from random import randint
from logger import Logger
from Organizmy.organizm import Organizm

log=Logger()
okno = Okno(log,(20,20))

#rozmiar=okno.wczytaj_rozmiar()

rozmiar=(20,20)
#rozmiar jest tuplą, ma w sobie (szerokość, wysokość)

swiat=Swiat(rozmiar, log)
okno.setSwiat(swiat)
# mam nadzieje ze działa

okno.symulacja()
