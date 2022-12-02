#Zilon Huang & Joran Middelman

from tkinter import Frame, Label, Entry, Tk, Button
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage 
from PIL import Image
import math

#initialise the window
scherm = Frame() #Setting up frame
scherm.master.title("Mandelbrot")
scherm.configure(width=420,height=550)
scherm.pack()

#setup of midden x:
tekst = Label(scherm, text="Midden x:", font=("Arial", 18)); tekst.place(x=10, y=10);
InvoerMiddenX  = Entry(scherm, width=10); InvoerMiddenX.place(x=100, y=10);

#setup of midden y:
tekst = Label(scherm, text="midden y:", font=("Arial", 18)); tekst.place(x=10, y=40);
InvoerMiddenY = Entry(scherm, width=10); InvoerMiddenY.place(x=100, y=40);

#setup of schaal:
tekst = Label(scherm, text="schaal:", font=("Arial", 18)); tekst.place(x=10, y=70);
InvoerSchaal = Entry(scherm, width=10); InvoerSchaal.place(x=100, y=70);

#setup of iterations:
tekst = Label(scherm, text="iteraties:", font=("Arial", 18)); tekst.place(x=10, y=100);
InvoerIteraties = Entry(scherm, width=10); InvoerIteraties.place(x=100, y=100);

#setup van de knop
knop = Button(scherm, text="Bereken", font=("Arial, 18"), height=5,width=10); knop.place(x=240,y=10);

# Afbeelding van Mandelbrot
afbeelding = Label(scherm); afbeelding.place(x=10,y=140)
# Aantal pixels in de x en y richting
width_x, height_y = 400, 400

def calc(c1, c2):
    x = y = 0
    for i in range(maxIt):
        x, y = x*x - y*y + c1, 2*x*y + c2
        if x*x + y*y > 4:
            return i+1
    return 0

def teken():
    plaatje = Image.new(mode="RGB", size=(width_x,height_y))
    draw = Draw(plaatje)
    
    for row in range(width_x):
        c1 = (row-200) * schaal + CoordinaatX
        for col in range(height_y):
            c2 = (col-200) * schaal + CoordinaatY
            v = calc(c1,c2)
            if v:
              plaatje.putpixel((row, col), (255,255,0))
              
    global omgezetPlaatje
    omgezetPlaatje = PhotoImage(plaatje)
    afbeelding.configure(image=omgezetPlaatje)

# Declaratie van globale variables
CoordinaatX = 0; CoordinaatY = 0;schaal = 0; maxIt = 0

def bereken():
    global CoordinaatX, CoordinaatY,schaal,maxIt
    try:
        CoordinaatX = float(InvoerMiddenX.get())
        CoordinaatY= float(InvoerMiddenY.get())
        schaal=float(InvoerSchaal.get())
        maxIt=int(InvoerIteraties.get())
        teken()
    except:
        CoordinaatX = 0.0
        CoordinaatY= 0.0
        schaal= 0.00
        maxIt= 0
        teken()
        
knop.configure(command=bereken)

bereken()

scherm.mainloop()

# if(mandelnummer % 2 != 0):
#                 plaatje.putpixel((row, col), (0 , 0, 0))
#             else:
#                 hue = int(255 * mandelnummer / maxIt)
#                 saturation = 255
#                 value = 255 if mandelnummer < maxIt else 0
#             plaatje.putpixel((row, col),(hue, saturation, value))  
