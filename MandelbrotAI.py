#Zilon Huang & Joran Middelman

#import benodigde libraries
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
InvoerMiddenX  = Entry(scherm, width=10); InvoerMiddenX.place(x=100, y=10); InvoerMiddenX.insert(0,str(0));

#setup of midden y:
tekst = Label(scherm, text="midden y:", font=("Arial", 18)); tekst.place(x=10, y=40);
InvoerMiddenY = Entry(scherm, width=10); InvoerMiddenY.place(x=100, y=40); InvoerMiddenY.insert(0,str(0));

#setup of schaal:
tekst = Label(scherm, text="schaal:", font=("Arial", 18)); tekst.place(x=10, y=70);
InvoerSchaal = Entry(scherm, width=10); InvoerSchaal.place(x=100, y=70); InvoerSchaal.insert(0,str(0.01));

#setup of iterations:
tekst = Label(scherm, text="iteraties:", font=("Arial", 18)); tekst.place(x=10, y=100);
InvoerIteraties = Entry(scherm, width=10); InvoerIteraties.place(x=100, y=100); InvoerIteraties.insert(0,str(20));

#setup van de knop
knop = Button(scherm, text="Bereken", font=("Arial, 18"), height=5,width=10); knop.place(x=240,y=10);

# Afbeelding van Mandelbrot
afbeelding = Label(scherm); afbeelding.place(x=10,y=140)

# Aantal pixels in de x en y richting
width_x, height_y = 400, 400

# toepassen van de formule en condities 
def calc(x, y):
    a = 0; b = 0; mandelgetal = 0; pythagoras = 0
    while pythagoras <= 2 and mandelgetal <= maxIt: #Afstand niet groter dan 2 en functie stopt als het bij de aangegeven max. iteraties komt. 
        pythagoras = math.sqrt(a*a + b*b) # Berekend de afstand
        a, b = a*a - b*b + x, 2*a*b + y # functie van de opgave
        mandelgetal += 1 # Het mandelgetal van aantal keer dat f is toegepast
        
    if mandelgetal == 1: # Conditie als het mandel getal al 1 is dan geeft hij gelijk 1 terug
        return 1
    elif mandelgetal == maxIt: # Conditie als mandelgetal oneindig is dan stoppen we met het toepassen van de functie en zetten we het mandelgetal op max iteraites
        return maxIt
    else:
        return mandelgetal # Als de vorige niet voordoen dan is het mandelgetal tussen 1 en maxIt

def teken():
    plaatje = Image.new(mode="RGB", size=(width_x,height_y))
    draw = Draw(plaatje)
    
    for row in range(width_x):
        x = (row-200) * schaal + CoordinaatX
        for col in range(height_y):
            y = (col-200) * schaal + CoordinaatY
            
            v = calc(x,y)
            if(v % 2 != 0):
                plaatje.putpixel((row, col), (0 , 0, 0))
            else:
                plaatje.putpixel((row, col), (255 , 255, 255))
            #else:
            # hue = int(255 * v / maxIt)
            # saturation = 255
            # value = 255 if v < maxIt else 0
            # plaatje.putpixel((row, col),(hue, saturation, value))  

    global omgezetPlaatje
    omgezetPlaatje = PhotoImage(plaatje)
    afbeelding.configure(image=omgezetPlaatje)

# Declaratie van globale variables
CoordinaatX = 0; CoordinaatY = 0;schaal = 0; maxIt = 0

def bereken(): # functie vraagt de input van de gebruiker en pas ze toe in de functie teken()
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
