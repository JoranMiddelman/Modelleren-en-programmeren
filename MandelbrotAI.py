#python3.11 -m venv "virtual omgeving"
#source virtual/bin/activate
#pip3 install "library"

#Zilon Huang & Joran Middelman

from tkinter import Frame, Label, Entry, Tk, Button
import math
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage 
from PIL import Image

#initialise the window
scherm = Tk()
scherm.geometry("420x550")
scherm.title("Mandelbrot")

#setup of midden x:
tekst = Label(scherm)
tekst.place(x=10, y=10)
tekst.configure(text="Midden x:", font=("Arial", 18))

mx = invoer = Entry(scherm)
invoer.place(x=100, y=10)
invoer.configure(width=10)

#setup of midden y:
tekst = Label(scherm)
tekst.place(x=10, y=40)
tekst.configure(text="midden y:", font=("Arial", 18))

my = invoer = Entry(scherm)
invoer.place(x=100, y=40)
invoer.configure(width=10)

#setup of schaal:
tekst = Label(scherm)
tekst.place(x=10, y=70)
tekst.configure(text="schaal:", font=("Arial", 18))

s = invoer = Entry(scherm)
invoer.place(x=100, y=70)
invoer.configure(width=10)

#setup of iterations:
tekst = Label(scherm)
tekst.place(x=10, y=100)
tekst.configure(text="iteraties:", font=("Arial", 18))

w = invoer = Entry(scherm)
invoer.place(x=100, y=100)
invoer.configure(width=10)

#setup van de knop
knop = Button(scherm)
knop.place(x=240,y=10)
knop.configure(text="Bereken",font=("Arial, 18"),height=5,width=10)

#Setup van mandelbrot plaatje
xbegin = -2.0
xwidth = 3
ystart = -1.5
yheight = 3
maxIt = 50 # max iterations allowed
Pixelscale = 200

image_width = int(Pixelscale*xwidth)
image_height = int(Pixelscale*yheight)

# Afbeelding van Mandelbrot
width_x= 400
height_y = 400

afbeelding = Label(scherm) 
afbeelding.place(x=10,y=140) 

plaatje = Image.new(mode="RGB", size=(image_width,image_height))
draw = Draw(plaatje)
    
def calc(c1, c2):
    x = y = 0
    for i in range(maxIt):
        x, y = x*x - y*y + c1, 2*x*y + c2
        if x*x + y*y > 4:
            return i+1
    return 0

for row in range(image_width):
    c1 = xbegin + row/Pixelscale
    for col in range(image_height):
        c2 = ystart + col/Pixelscale
        v = calc(c1, c2)
        if v:
            plaatje.putpixel((row, col), (255,255,0))


    
omgezetPlaatje = PhotoImage(plaatje)
afbeelding.configure(image=omgezetPlaatje)

#def bereken():
# p=mx.get()
# l=my.get()
# k=s.get()
# m=w.get()
 
# print(p)
# print(l)
# print(k)
# print(m)
 
#knop.configure(command=bereken)
scherm.mainloop()