from tkinter import Label, filedialog
from Schets import Schets
from PIL import ImageGrab
            
class SchetsControl(Label):
    def __init__(self,parent):
        super().__init__(parent)
        self.bind("<Configure>", self.vergroot)
        self.schets = Schets()
        self.kleur = "black"

    def vergroot(self, ea):
        wh = (self.winfo_width(), self.winfo_height())
        self.schets.VeranderAfmeting(wh)
        self.Teken()

    def Teken(self):
        self.foto = self.schets.Tekening()
        self.configure(image=self.foto)

    def Schoon(self):
        self.schets.Schoon()
        self.Teken()

    def Roteer(self):
        self.schets.Roteer()
        self.Teken()

    def VeranderKleur(self, k):
        self.kleur = k

      # opslaan van afbeelding
    def Opslaan(self):
        self.afbeeldingnaam = filedialog.asksaveasfile(initialfile="naam.png", defaultextension="png", filetypes=[("PNG",".png"),("JPG",".jpg"),("BMP",".bmp")])
