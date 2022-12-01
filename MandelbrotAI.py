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

InvoerMiddenX = invoer = Entry(scherm)
invoer.place(x=100, y=10)
invoer.configure(width=10)

#setup of midden y:
tekst = Label(scherm)
tekst.place(x=10, y=40)
tekst.configure(text="midden y:", font=("Arial", 18))

InvoerMiddenY = invoer = Entry(scherm)
invoer.place(x=100, y=40)
invoer.configure(width=10)

#setup of schaal:
tekst = Label(scherm)
tekst.place(x=10, y=70)
tekst.configure(text="schaal:", font=("Arial", 18))

InvoerSchaal = invoer = Entry(scherm)
invoer.place(x=100, y=70)
invoer.configure(width=10)

#setup of iterations:
tekst = Label(scherm)
tekst.place(x=10, y=100)
tekst.configure(text="iteraties:", font=("Arial", 18))

InvoerIteraties = invoer = Entry(scherm)
invoer.place(x=100, y=100)
invoer.configure(width=10)

#setup van de knop
knop = Button(scherm)
knop.place(x=240,y=10)
knop.configure(text="Bereken",font=("Arial, 18"),height=5,width=10)

#Setup van mandelbrot plaatje
maxIt = 20 # max iterations allowed

# Afbeelding van Mandelbrot
width_x= 400
height_y = 400

afbeelding = Label(scherm) 
afbeelding.place(x=10,y=140) 

def calc(c1, c2):
    x = y = 0
    for i in range(maxIt):
        x, y = x*x - y*y + c1, 2*x*y + c2
        if x*x + y*y > 4:
            return i+1
    return 0

def teken(schaal):
    plaatje = Image.new(mode="RGB", size=(width_x,height_y))
    draw = Draw(plaatje)
    for row in range(width_x):
        c1 = (row-200) * schaal
        for col in range(height_y):
            c2 = (col-200) * schaal
            v = calc(c1,c2)
            if v:
              plaatje.putpixel((row, col), (255,255,0))        
    global omgezetPlaatje
    omgezetPlaatje = PhotoImage(plaatje)
    afbeelding.configure(image=omgezetPlaatje)

def bereken():
    
    CoordinaatX = InvoerMiddenX.get()
    CoordinaatY=InvoerMiddenY.get()
    schaal=InvoerSchaal.get()
    Iter=InvoerIteraties.get()
        
    print(CoordinaatX)
    print(CoordinaatY)
    print(schaal)
    print(Iter)
 
    teken(float(schaal))
 
knop.configure(command=bereken)
teken(0.01)
scherm.mainloop()
