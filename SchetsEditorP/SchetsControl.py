from tkinter import Label, messagebox, filedialog
from Schets import Schets
from PIL import Image

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
        
    # Opslaan van afbeelding
    def Opslaan(self):
        afbeeldingnaam = filedialog.asksaveasfile(initialfile="leeg.png", defaultextension=".png", filetypes=[("PNG",".png"),("JPG",".jpg"),("BMP",".bmp")])
        if afbeeldingnaam:
            self.schets.bitmap.save("afbeelding.png")

