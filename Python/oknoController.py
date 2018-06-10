from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Scrollbar
from tkinter import Listbox
import swiat

class Okno:


    def __init__(self, log, r=(0,0)):
        self._szerokosc=r[0]
        self._wysokosc=r[1]
        self._rozmiarPola=30
        self._master=None
        self._c_plansza=None
        self._swiat=None
        self._logger=log
        self._listbox=None

        self._klawisz = None

    def setSwiat(self, s):
        self._swiat=s

    def setImages(self):
        self.owca = PhotoImage(file="img\owca.png")
        self.zolw = PhotoImage(file="img\zolw.png")
        self.wilk = PhotoImage(file="img\wilk.png")
        self.antylopa = PhotoImage(file="img\Antylopa.png")
        self.cyber_owca = PhotoImage(file="img\cyber_owca.png")
        self.czlowiek = PhotoImage(file="img\czlowiek.png")
        self.lis = PhotoImage(file="img\lis.png")
        self.mlecz = PhotoImage(file="img\mlecz.png")
        self.trawa = PhotoImage(file="img\Trawa.png")
        self.guarana = PhotoImage(file="img\guarana.png")
        self.wilcza_jagoda = PhotoImage(file="img\wilcza_jagoda.png")
        self.barszcz = PhotoImage(file="img\Barszcz.png")

    def wczytaj_rozmiar(self):
        master=Tk()

        def select():
            sel_h = "Wysokość = " + str(var_height.get())
            label_h.config(text=sel_h)
            sel_w = "Szerokość = " + str(var_width.get())
            label_w.config(text=sel_w)
            answer = messagebox.askokcancel("Wybrano rozmiar", "Czy chcesz kontynuować?")
            if(answer==True and var_height.get()!=0 and var_width.get()!=0):
                master.destroy()




        master.title("Podaj rozmiar")
        master.geometry("200x200")

        var_height=IntVar()
        var_width=IntVar()

        height_scale=Scale(master, variable=var_height)
        height_scale.place(x=5, y=20)

        width_scale=Scale(master, variable=var_width)
        width_scale.place(x=135, y=20)


        button=Button(master, text="Ustaw rozmiar", command=select)
        button.pack()

        label_h=Label(master)
        label_h.pack()
        label_w=Label(master)
        label_w.pack()
        master.mainloop()
        self._szerokosc=var_width.get()
        self._wysokosc=var_height.get()
        return (int(var_width.get()),int(var_height.get()))

    def zapisz(self):
        plik = simpledialog.askstring("Zapisywanie", "Podaj nazwę pliku", parent=self._master)
        print("Zapis!")
        print(plik)

    def wczytaj(self):
        plik=simpledialog.askstring("Wczytywanie","Podaj nazwę pliku", parent=self._master)
        print("Wczytaj!")
        print(plik)

    def nowaTura(self):
        self._swiat.wykonajTure()
        self._logger.czyscLog()
        self._c_plansza.delete(ALL)
        self.rysujPlansze()
        self.umiescZdjecia()
        self._listbox.delete(0, END)
        for i in self._logger.getLog():
            self._listbox.insert(END, i)

        self._klawisz = ""
        print("Nowa tura!")

    def rysujPlansze(self):
        for i in range(0, self._wysokosc):
            self._c_plansza.create_line(0, i * self._rozmiarPola, self._szerokosc * self._rozmiarPola,
                                        i * self._rozmiarPola)
        for i in range(0, self._szerokosc):
            self._c_plansza.create_line(i * self._rozmiarPola, 0, i * self._rozmiarPola, self._wysokosc * self._rozmiarPola)

    def umiescZdjecia(self):
        plansza = self._swiat.getPlansza()
        for y in range(0, self._wysokosc):
            for x in range(0, self._szerokosc):
                obraz = None
                znak = None
                if(self._swiat.getOrganizmAtXY(x,y)!=None):
                    znak = self._swiat.getOrganizmAtXY(x,y).getSymbol()
                if znak != None:
                    if znak == 'Z':
                        obraz = self.zolw
                    elif znak == 'A':
                        obraz = self.antylopa
                    elif znak == 'W':
                        obraz = self.wilk
                    elif znak == 'L':
                        obraz = self.lis
                    elif znak == 'O':
                        obraz = self.owca
                    elif znak == 'C':
                        obraz = self.cyber_owca
                    elif znak == '@':
                        obraz = self.czlowiek
                    elif znak == 'T':
                        obraz = self.trawa
                    elif znak == 'G':
                        obraz = self.guarana
                    elif znak == 'M':
                        obraz = self.mlecz
                    elif znak == 'J':
                        obraz = self.wilcza_jagoda
                    elif znak == 'B':
                        obraz = self.barszcz

                self._c_plansza.create_image(x * self._rozmiarPola, y * self._rozmiarPola, image=obraz,
                                             anchor=NW)

    def symulacja(self):
        self._master=Tk()
        self._master.title("Symulacja")
        self._master.resizable(0,0)
        self.setImages()
        def left(e):
            self._klawisz="left"
            print("left key")
            self.nowaTura()
        def right(e):
            self._klawisz="right"
            print("right key")
            self.nowaTura()
        def up(e):
            self._klawisz="up"
            print("upper key")
            self.nowaTura()
        def down(e):
            self._klawisz="down"
            print("down key")
            self.nowaTura()
        def ability(e):
            _klawisz="q"
            print("special ability")
        def click(e):
            x=e.x
            y=e.y
            wspolrzedne_xy=(x//self._rozmiarPola, y//self._rozmiarPola)
            print(wspolrzedne_xy)

        self._c_plansza = Canvas(self._master, bg="grey", width=self._rozmiarPola * self._szerokosc,
                           height=self._rozmiarPola * self._wysokosc)
        self._c_plansza.pack(side="bottom")

        self.rysujPlansze()
        self.umiescZdjecia()

        scrollbar = Scrollbar(self._master)
        self._listbox = Listbox(self._master, bd=0, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self._listbox.yview)


        self._master.bind("<Left>", left)
        self._master.bind("<Right>", right)
        self._master.bind("<Up>", up)
        self._master.bind("<Down>", down)
        self._master.bind("<q>", ability)
        self._master.bind("<Q>", ability)
        self._c_plansza.bind("<Button 1>", click)

        b_zapisz=Button(self._master, text="Zapisz", command=self.zapisz)
        b_wczytaj=Button(self._master, text="Wczytaj", command=self.wczytaj)
        b_nowa_tura=Button(self._master, text="Nowa Tura", command=self.nowaTura)

        #ustawianie rozmiaru okna
        if(self._rozmiarPola*self._szerokosc<300):
            self._master.geometry("300x"+str(self._rozmiarPola*self._wysokosc+300))
            b_zapisz.place(x=0, y=0, width=100, height=40)
            b_wczytaj.place(x=100, y=0, width=100, height=40)
            b_nowa_tura.place(x=200, y=0, width=100, height=40)
            self._listbox.place(x=0, y=50, width=300, height=200)
        else:
            self._master.geometry(str(self._rozmiarPola*self._szerokosc)+"x"+str(self._rozmiarPola*self._wysokosc+300))
            pol_x = (self._rozmiarPola * self._szerokosc - 300) / 2
            b_zapisz.place(x=pol_x, y=0, width=100, height=40)
            b_wczytaj.place(x=pol_x + 100, y=0, width=100, height=40)
            b_nowa_tura.place(x=pol_x + 200, y=0, width=100, height=40)
            self._listbox.place(x=pol_x, y=50, width=300, height=200)


        self._master.mainloop()

    def getKlawisz(self):
        return self._klawisz