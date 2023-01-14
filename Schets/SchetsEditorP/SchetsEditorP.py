from tkinter import Frame, Menu
from SchetsWin import SchetsWin
from tkinter.messagebox import showinfo

class SchetsEditorP(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("SchetsEditorP")
        self.configure(background="lightblue")
        self.configure(width=200, height=100)
        self.pack()

        menubar = Menu(self)
        self.maakFileMenu(menubar)
        self.maakHelpMenu(menubar)

    def maakFileMenu(self, menubar):
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nieuw...", command=self.nieuw)
        filemenu.add_command(label="Exit",     command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.configure(menu=menubar)

    def maakHelpMenu(self, menubar):
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Over \"Schets\"", command=self.about)
        menubar.add_cascade(label="Help", menu=filemenu)
        self.master.configure(menu=menubar)

    def nieuw(self):
        tekst = SchetsWin(self)

    def about(self):
        showinfo(title="Over \"Schets\"", message="Schets versie 2.0P\n(c) UU Informatica 2022" )
