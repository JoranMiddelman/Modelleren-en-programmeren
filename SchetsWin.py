from tkinter       import Toplevel, Menu, Frame, Label, Button, Radiobutton, Listbox, IntVar, ttk
from PIL.ImageTk   import PhotoImage
from PIL           import Image
from SchetsControl import SchetsControl
from Tools         import PenTool, LijnTool, RechthoekTool, VolRechthoekTool, TekstTool, GumTool, OvaalTool, VolOvaalTool

class SchetsWin(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("800x600")

        deTools = [PenTool(), LijnTool(), RechthoekTool(), VolRechthoekTool(), TekstTool(), GumTool(), OvaalTool(), VolOvaalTool()]
        deKleuren = ["black", "red", "green", "blue", "yellow", "magenta", "cyan"]

        self.huidigeTool = deTools[0]

        paneel = Frame(self)
        paneel.pack(side="left", padx=10)

        self.schetscontrol = SchetsControl(self)
        self.schetscontrol.pack(fill="both", expand=True)
        self.schetscontrol.bind("<Button-1>", self.mousedown)
        self.schetscontrol.bind("<ButtonRelease-1>", self.mouseup)
        self.schetscontrol.bind("<Motion>", self.mousemove)
        self.bind("<Key>", self.keypress)

        menubar = Menu(self)
        self.maakFileMenu(menubar)
        self.maakToolMenu(menubar, deTools)
        self.maakActieMenu(menubar, deKleuren)
        self.maakToolButtons(paneel, deTools)
        self.maakActieButtons(paneel, deKleuren)
        self.configure(menu=menubar)

        self.vast = False

    def mousedown(self, ea):
        self.vast = True
        self.huidigeTool.MuisVast(self.schetscontrol, (ea.x, ea.y))

    def mouseup(self, ea):
        if self.vast:
            self.huidigeTool.MuisLos(self.schetscontrol, (ea.x, ea.y))
        self.vast = False

    def mousemove(self, ea):
        if self.vast:
            self.huidigeTool.MuisDrag(self.schetscontrol, (ea.x, ea.y))

    def keypress(self, ea):
        c = ea.char
        if c and ord(c)>=32:
            self.huidigeTool.Letter(self.schetscontrol, c)

    def selecteerTool(self, t):
        self.huidigeTool = t

    def VeranderKleurCbb(self, ea):
        self.schetscontrol.VeranderKleur(ea.widget.get())

    def VeranderKleurLb(self, ea):
        t = ea.widget.curselection()
        if len(t)>0:
            self.schetscontrol.VeranderKleur(ea.widget.get(t[0]))

    def maakFileMenu(self, menubar):
        menu = Menu(menubar, tearoff=0)
        menu.add_command(label="Sluiten", command=self.destroy)
        menubar.add_cascade(label="File", menu=menu)

    def maakToolMenu(self, menubar, tools):
        menu = Menu(menubar, tearoff=0)
        for tool in tools:
            naam = str(tool)
            menu.add_command(label=naam, command=lambda t=tool:self.selecteerTool(t))
        menubar.add_cascade(label="Tool", menu=menu)

    def maakActieMenu(self, menubar, kleuren):
        menu = Menu(menubar, tearoff=0)
        menu.add_command(label="Clear", command=self.schetscontrol.Schoon)
        submenu =Menu(menu, tearoff=0)
        for kleur in kleuren:
            submenu.add_command(label=kleur, command=lambda k=kleur:self.schetscontrol.VeranderKleur(k))
        menu.add_cascade(label="Kies kleur", menu=submenu)
        menubar.add_cascade(label="Actie", menu=menu)

    def maakActieButtons(self, box, kleuren):
        lb = Listbox(box, height=len(kleuren))
        for kleur in kleuren:
            lb.insert("end", kleur)
        lb.select_set(0)
        lb.pack(pady=5)
        lb.bind("<<ListboxSelect>>", self.VeranderKleurLb)
        # cbb = ttk.Combobox(box, values=kleuren)
        # cbb.current(0)
        # cbb.pack()
        # cbb.bind("<<ComboboxSelected>>", self.VeranderKleurCbb)

        clear = Button(box, text="Clear", command=self.schetscontrol.Schoon)
        clear.pack(pady=5)
        roteer = Button(box, text="Rotate", command=self.schetscontrol.Roteer)
        roteer.pack(pady=5)

    def maakToolButtons(self, box, tools):
        t = 0
        self.gekozenButton = IntVar(box, value=0)
        for tool in tools:
            naam = str(tool)
            tool.afb = PhotoImage(Image.open(f"Icons/{naam}.png"))
            b = Radiobutton(box, text=str(tool), value=t, variable=self.gekozenButton, image=tool.afb, compound="bottom", command=lambda t=tool:self.selecteerTool(t))
            b.pack()
            t = t+1
