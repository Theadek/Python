from oknoController import Okno
from random import randint

okno = Okno()
#wczytywanie rozmiaru, na razie na sztywno ustawiam 20 x 20
#rozmiar=okno.wczytaj_rozmiar()
okno._szerokosc=20
okno._wysokosc=20
#rozmiar jest tuplą, ma w sobie (szerokość, wysokość)
#swiat=Swiat(rozmiar)

okno.symulacja()

