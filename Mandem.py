#Zilon Huang & Joran Middelman

from tkinter import Frame, Label, Entry, Tk, Button
import math
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage 
from PIL import Image

#initialise the window
scherm = Tk()
scherm.geometry("600x600")
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

i = invoer = Entry(scherm)
invoer.place(x=100, y=100)
invoer.configure(width=10)

#setup van de knop
knop = Button(scherm)
knop.place(x=240,y=10)

knop.configure(text="Bereken",font=("Arial, 18"),height=5,width=10)


#Setup van mandelbrot plaatje
plaatje = Image.new(mode="RGBA", size=(400,400))
afbeelding = Label(scherm)
afbeelding.place(x=10,y=140)
afbeelding.configure(background="white")
draw = Draw(plaatje)

def TekenHuis(x,y,breedte):
    topx = x+breedte/2
    topy = y-3*breedte/2
    afdak = breedte/6
    randy = y-breedte+afdak
    
    draw.rectangle(((x,y-breedte),(x+breedte,y)), fill="lightgreen",outline ="green")
    draw.line( ((x-afdak, randy), (topx, topy)), fill="red", width=3)
    draw.line( ((topx, topy), (x+breedte+afdak, randy)), fill="red", width=3)
    
TekenHuis( 20, 100, 40)
TekenHuis( 80, 100, 40)
TekenHuis(140, 100, 60)  

omgezetPlaatje = PhotoImage(plaatje) 
afbeelding.configure(image=omgezetPlaatje)

#Width = 400
#Height = 400

#Px = []
#Py =[]

#for Px in Width and Py in Height:
#    Px < Width
#    Px += 1
#    
#    Py < Height
#   Px += 1

#    x0 = 0
#    y0 = 0
#
#    x = 0
#    y = 0
#    iteration = 0
#    maxiter = 10

#    while (x*x + y*y <= 4 and iteration < maxiter):
#     xtemp = 2*x*y + y0
#     y = 2*x*y + y0
#     x = xtemp
#     iteration += 1


scherm.mainloop()
