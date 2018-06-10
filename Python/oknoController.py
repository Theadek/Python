from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Scrollbar
from tkinter import Listbox
import swiat
import pickle

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
        self._b_zapisz = None
        self._b_wczytaj = None
        self._b_nowa_tura = None
        self._b_nowa_gra = None
        self._new_window_blocked=False
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
        if plik != None:
            with open(str(plik)+".pickle", 'wb') as handle:
                pickle.dump(self._swiat, handle)

    def wczytaj(self):
        plik=simpledialog.askstring("Wczytywanie","Podaj nazwę pliku", parent=self._master)
        try:
            with open(str(plik) + ".pickle", 'rb') as handle:
                self._swiat = pickle.load(handle)
            self._logger=self._swiat._logger
            self._szerokosc=self._swiat.getWidth()
            self._wysokosc=self._swiat.getHeight()
            self._c_plansza.delete(ALL)
            self._c_plansza.pack_forget()
            self.ustawRozmiarOkna()
            self.rysujPlansze()
            self.umiescZdjecia()
            self._listbox.delete(0, END)
            for i in self._logger.getLog():
                self._listbox.insert(END, i)
        except FileNotFoundError:
          messagebox.showinfo("Błąd","Nie ma takiego pliku!")


    def nowaTura(self):
        self._logger.czyscLog()
        self._swiat.wykonajTure()
        self._c_plansza.delete(ALL)
        self.rysujPlansze()
        self.umiescZdjecia()
        self._listbox.delete(0, END)
        for i in self._logger.getLog():
            self._listbox.insert(END, i)

        self._swiat.setKlawisz("")
        print("Nowa tura!")

    def nowaGra(self):
        self._swiat.usun_wszystko()
        self._c_plansza.delete(ALL)
        self._swiat.losuj(2)
        self.rysujPlansze()
        self.umiescZdjecia()
        self._listbox.delete(0, END)

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

    def ustawRozmiarOkna(self):
        if (self._rozmiarPola * self._szerokosc < 300):
            self._master.geometry("300x" + str(self._rozmiarPola * self._wysokosc + 300))
            self._b_zapisz.place(x=0, y=0, width=75, height=40)
            self._b_wczytaj.place(x=75, y=0, width=75, height=40)
            self._b_nowa_tura.place(x=150, y=0, width=75, height=40)
            self._b_nowa_gra.place(x=225, y=0, width=75, height=40)
            self._listbox.place(x=0, y=50, width=300, height=200)
            self._c_plansza = Canvas(self._master, bg="grey", width=self._rozmiarPola * self._szerokosc,
                                     height=self._rozmiarPola * self._wysokosc)
            self._c_plansza.pack(side="bottom")
        else:
            self._master.geometry(
                str(self._rozmiarPola * self._szerokosc) + "x" + str(self._rozmiarPola * self._wysokosc + 300))
            pol_x = (self._rozmiarPola * self._szerokosc - 300) / 2
            self._b_zapisz.place(x=pol_x, y=0, width=75, height=40)
            self._b_wczytaj.place(x=pol_x + 75, y=0, width=75, height=40)
            self._b_nowa_tura.place(x=pol_x + 150, y=0, width=75, height=40)
            self._b_nowa_gra.place(x=pol_x + 225, y=0, width=75, height=40)
            self._listbox.place(x=pol_x, y=50, width=300, height=200)
            self._c_plansza = Canvas(self._master, bg="grey", width=self._rozmiarPola * self._szerokosc,
                                     height=self._rozmiarPola * self._wysokosc)
            self._c_plansza.pack(side="bottom")

    def dodajOrganizm(self, wspolrzedne_xy):
        def sel():
            self._new_window_blocked = False
            zn = str(var.get())
            self._swiat.makeOrganizm(wspolrzedne_xy[0], wspolrzedne_xy[1], zn)
            self.umiescZdjecia()
            root.destroy()

        root = Tk()
        var = StringVar(master=root)

        List=[]
        Gatunki=["Antylopa", "Cyber-owca", "Owca", "Wilk", "Lis", "Zolw","Trawa","Guarana", "Mlecz", "Barszcz", "Jagoda"]
        for i in range(0,11):
            List.append(Radiobutton(root, text=Gatunki[i], variable=var, value=Gatunki[i][:1],
                         command=sel,tristatevalue=0))
            List[i].pack(anchor="w")

        label = Label(root)
        label.pack()
        root.mainloop()

    def symulacja(self):
        self._master=Tk()
        self._master.title("Symulacja")
        self._master.resizable(0,0)
        self.setImages()
        def left(e):
            self._swiat.setKlawisz("left")
            print("left key")
            self.nowaTura()
        def right(e):
            self._swiat.setKlawisz("right")
            print("right key")
            self.nowaTura()
        def up(e):
            self._swiat.setKlawisz("up")
            print("upper key")
            self.nowaTura()
        def down(e):
            self._swiat.setKlawisz("down")
            print("down key")
            self.nowaTura()
        def ability(e):
            self._swiat.setKlawisz("q")
            print("special ability")
            self.nowaTura()
        def click(e):
            if self._new_window_blocked==False:
                self._new_window_blocked=True
                x=e.x
                y=e.y
                wspolrzedne_xy=(x//self._rozmiarPola, y//self._rozmiarPola)
                self.dodajOrganizm(wspolrzedne_xy)
                self._swiat.makeOrganizm(wspolrzedne_xy[0], wspolrzedne_xy[1],self._zn)

        scrollbar = Scrollbar(self._master)
        self._listbox = Listbox(self._master, bd=0, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self._listbox.yview)




        self._b_zapisz=Button(self._master, text="Zapisz", command=self.zapisz)
        self._b_wczytaj=Button(self._master, text="Wczytaj", command=self.wczytaj)
        self._b_nowa_tura=Button(self._master, text="Nowa Tura", command=self.nowaTura)
        self._b_nowa_gra=Button(self._master, text="Nowa Gra", command=self.nowaGra)

        #ustawianie rozmiaru okna
        self.ustawRozmiarOkna()
        self.rysujPlansze()
        self.umiescZdjecia()

        self._master.bind("<Left>", left)
        self._master.bind("<Right>", right)
        self._master.bind("<Up>", up)
        self._master.bind("<Down>", down)
        self._master.bind("<q>", ability)
        self._master.bind("<Q>", ability)
        self._c_plansza.bind("<Button 1>", click)


        self._master.mainloop()

    def getKlawisz(self):
        return self._klawisz