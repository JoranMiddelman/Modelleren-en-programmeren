from PIL.ImageDraw import Draw
from PIL.ImageTk   import PhotoImage
from PIL           import Image


class Schets:
    def __init__(self):
        self.bitmap = Image.new(mode="RGBA", size=(1,1), color="white")

    def VeranderAfmeting(self, wh):
        nieuweBitmap = Image.new(mode="RGBA", size=wh, color="white")
        nieuweBitmap.paste(self.bitmap, (0,0))
        self.bitmap = nieuweBitmap

    def Tekening(self):
        return PhotoImage(self.bitmap)

    def Schoon(self):
        self.bitmap = Image.new(mode="RGBA", size=(self.bitmap.width, self.bitmap.height), color="white")

    def Roteer(self):
        self.bitmap = self.bitmap.rotate(90)
