from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


class Okno:

    def __init__(self):
        self._szerokosc=0
        self._wysokosc=0
        self._rozmiarPola=30
        self._master=None


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
        print("Nowa tura!")

    def symulacja(self):
        self._master=Tk()
        self._master.title("Symulacja")
        self._master.resizable(0,0)
        def left(e):
            print("left key")
        def right(e):
            print("right key")
        def up(e):
            print("upper key")
        def down(e):
            print("down key")
        def ability(e):
            print("special ability")
        def click(e):
            x=e.x
            y=e.y
            wspolrzedne_xy=(x//self._rozmiarPola, y//self._rozmiarPola)
            print(wspolrzedne_xy)
        def rysujPlansze():
            for i in range(0,self._szerokosc):
                c_plansza.create_line(0,i*self._rozmiarPola, self._wysokosc*self._rozmiarPola, i*self._rozmiarPola)
            for i in range(0,self._wysokosc):
                c_plansza.create_line(i*self._rozmiarPola,0, i*self._rozmiarPola, self._szerokosc*self._rozmiarPola)


        c_plansza = Canvas(self._master, bg="red", width=self._rozmiarPola * self._szerokosc,
                           height=self._rozmiarPola * self._wysokosc)
        c_plansza.pack(side="bottom")
        rysujPlansze()

        self._master.bind("<Left>", left)
        self._master.bind("<Right>", right)
        self._master.bind("<Up>", up)
        self._master.bind("<Down>", down)
        self._master.bind("<q>", ability)
        c_plansza.bind("<Button 1>", click)

        b_zapisz=Button(self._master, text="Zapisz", command=self.zapisz)
        b_wczytaj=Button(self._master, text="Wczytaj", command=self.wczytaj)
        b_nowa_tura=Button(self._master, text="Nowa Tura", command=self.nowaTura)

        #ustawianie rozmiaru okna
        if(self._rozmiarPola*self._szerokosc<300):
            self._master.geometry("300x"+str(self._rozmiarPola*self._wysokosc+50))
            b_zapisz.place(x=0, y=0, width=100, height=40)
            b_wczytaj.place(x=100, y=0, width=100, height=40)
            b_nowa_tura.place(x=200, y=0, width=100, height=40)
        else:
            self._master.geometry(str(self._rozmiarPola*self._szerokosc)+"x"+str(self._rozmiarPola*self._wysokosc+50))
            pol_x = (self._rozmiarPola * self._szerokosc - 300) / 2
            b_zapisz.place(x=pol_x, y=0, width=100, height=40)
            b_wczytaj.place(x=pol_x + 100, y=0, width=100, height=40)
            b_nowa_tura.place(x=pol_x + 200, y=0, width=100, height=40)

        self._master.mainloop()