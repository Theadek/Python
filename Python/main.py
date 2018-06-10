from oknoController import Okno
from swiat import Swiat
from random import randint
from logger import Logger
from Organizmy.organizm import Organizm

log=Logger()
rozmiar=(15,15)
okno = Okno(log,rozmiar)

#rozmiar=okno.wczytaj_rozmiar()


#rozmiar jest tuplą, ma w sobie (szerokość, wysokość)

swiat=Swiat(rozmiar, log, okno)
okno.setSwiat(swiat)
# mam nadzieje ze działa

okno.symulacja()
