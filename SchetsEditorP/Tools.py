from SchetsControl import SchetsControl
from PIL.ImageFont import truetype
from PIL.ImageDraw import Draw
from PIL.ImageTk   import PhotoImage

class SchetsTool:
    def __init__(self):
        pass

class StartpuntTool(SchetsTool):
    def __init__(self):
        super().__init__()
        self.startpunt = (0,0)

    def MuisVast(self, sc, pt):
        self.startpunt = pt

    def MuisLos(self, sc, pt):
        self.kwast = sc.kleur

class TekstTool(StartpuntTool):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "tekst"
        
    def MuisDrag(self, sc, pt):
        pass

    def Letter(self, sc, c):
        draw = Draw(sc.schets.bitmap)
        font = truetype("tahoma.ttf", size=40)
        draw.text(self.startpunt, c, fill=sc.kleur, font=font)
        bb = draw.textbbox(self.startpunt, c, font=font)
        # draw.rectangle(bb, outline="red")
        (x1, y1, x2, y2) = bb
        (x, y) = self.startpunt
        self.startpunt = (x+x2-x1, y)
        sc.Teken()

class TweepuntTool(StartpuntTool):
    def __init__(self):
        super().__init__()

    def MuisVast(self, sc, pt):
        super().MuisVast(sc,pt)
        self.kwast = "grey"

    def MuisLos(self, sc, pt):
        super().MuisLos(sc,pt)
        self.Compleet(Draw(sc.schets.bitmap), self.startpunt, pt)
        sc.Teken()

    def MuisDrag(self, sc, pt):
        # maak een tijdelijke bitmap
        bm = sc.schets.bitmap.copy()
        # en teken daarop het draadfiguur
        self.Bezig(Draw(bm), self.startpunt, pt)
        # en display die bitmap op de schetscontrol
        sc.foto = PhotoImage(bm)
        sc.configure(image=sc.foto)

    def Letter(self, sc, c):
        pass

    def Compleet(self, draw, p1, p2):
        self.Bezig(draw, p1, p2)

class RechthoekTool(TweepuntTool):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "kader"

    def Bezig(self, draw, p1, p2):
        draw.rectangle((p1,p2), outline=self.kwast)

class VolRechthoekTool(RechthoekTool):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "vlak"

    def Compleet(self, draw, p1, p2):
        draw.rectangle((p1,p2), fill=self.kwast)

class LijnTool(TweepuntTool):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "lijn"

    def Bezig(self, draw, p1, p2):
        draw.line((p1,p2), fill=self.kwast, width=3)

class PenTool(LijnTool):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "pen"

    def MuisDrag(self, sc, pt):
        self.MuisLos(sc, pt)
        self.MuisVast(sc, pt)

class GumTool(PenTool):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "gum"

    def Bezig(self, draw, p1, p2):
        draw.line((p1,p2), fill="white", width=7)
        
    # Het toevoegen van een nieuwe class voor het maken van een eerst open en dan een gevulde ovaal
class OvaalTool(TweepuntTool):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "open-ovaal"
    
    def Bezig(self, draw, p1, p2):
        draw.ellipse((p1,p2), outline=self.kwast)
    
class VolOvaalTool(OvaalTool):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "gevulde-ovaal"
    
    def Compleet(self, draw, p1, p2):
        draw.ellipse((p1, p2), fill=self.kwast)
