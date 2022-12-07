#Zilon Huang & Joran Middelman

#Import benodigde libraries
from tkinter import *
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage 
from PIL import Image
import math

# Initialise the window we use to plot the image, invoer, slider, buttons
scherm = Frame()
scherm.master.title("Mandelbrot")
scherm.configure(width=620,height=550)
scherm.pack()

# Setup of midden x:
tekst = Label(scherm, text="Midden x:", font=("Arial", 18)); tekst.place(x=10, y=10);
InvoerMiddenX  = Entry(scherm, width=10); InvoerMiddenX.place(x=100, y=10); InvoerMiddenX.insert(0,str(0));

# Setup of midden y:
tekst = Label(scherm, text="Midden y:", font=("Arial", 18)); tekst.place(x=10, y=40);
InvoerMiddenY = Entry(scherm, width=10); InvoerMiddenY.place(x=100, y=40); InvoerMiddenY.insert(0,str(0));

# Setup of schaal:
tekst = Label(scherm, text="Schaal:", font=("Arial", 18)); tekst.place(x=10, y=70);
InvoerSchaal = Entry(scherm, width=10); InvoerSchaal.place(x=100, y=70); InvoerSchaal.insert(0,str(1e-2));

# Setup of iterations:
tekst = Label(scherm, text="Iteraties:", font=("Arial", 18)); tekst.place(x=10, y=100);
InvoerIteraties = Entry(scherm, width=10); InvoerIteraties.place(x=100, y=100); InvoerIteraties.insert(0,str(100));

# Setup van de knop
knop = Button(scherm, text="Bereken", font=("Arial, 18"), height=5,width=10); knop.place(x=210,y=10);

# Setup van de keuzemenu van vooraf bepaalde plaatjes
def keuze(): # Als deze functie wordt opgeroepen dan kijkt hij welke plaatje is gekozen door de gebruiker
    a = clicked.get() # Na het drukken van "Plaats de gekozen plaatje" wordt de keuze opgeslagen in variabel a
    if a == options[0]: # Kijk of de gekozen afbeelding in de eerste element is van de array. Zo niet gaat hij de lijst door.
        InvoerMiddenX.delete(0, 'end') # Verwijderd de input van de vorige invoer
        InvoerMiddenY.delete(0, 'end')
        InvoerIteraties.delete(0, 'end')
        InvoerSchaal.delete(0, 'end')

        InvoerMiddenX.insert(0,str(-0.40)) # Kent de waarde toe aan de entry 
        InvoerMiddenY.insert(0,str(-0.65))
        InvoerIteraties.insert(0,str(400))
        InvoerSchaal.insert(0,str(1e-3))
    elif a == options[1]:
        InvoerMiddenX.delete(0, 'end')
        InvoerMiddenY.delete(0, 'end')
        InvoerIteraties.delete(0, 'end')
        InvoerSchaal.delete(0, 'end')

        InvoerMiddenX.insert(0,str(-0.108625))
        InvoerMiddenY.insert(0,str(0.9014428))
        InvoerIteraties.insert(0,str(400))
        InvoerSchaal.insert(0,str(3.8147e-8))
    elif a == options[2]:                   # Gebruiken geen else want, 
        InvoerMiddenX.delete(0, 'end')      # we willen niet dat de functie automatisch naar de derde keuze gaat,
        InvoerMiddenY.delete(0, 'end')      # wanneer de gebruiker besluit niks te kiezen en toch besluit op de knop de drukken.
        InvoerIteraties.delete(0, 'end')
        InvoerSchaal.delete(0, 'end')

        InvoerMiddenX.insert(0,str(-0.2))
        InvoerMiddenY.insert(0,str(-0.65))
        InvoerIteraties.insert(0,str(400))
        InvoerSchaal.insert(0,str(1e-5))
    
options = [ 
           "Plaatje0",      # De verschillende keuze plaatjes
           "Plaatje1",
           "Plaatje2"
]

clicked = StringVar() # Container voor de keuze plaatjes 
clicked.set("Selecteer een plaatje") # Schrijft "selecteer een plaatje" op de menu in plaats van bijvoorbeeld "Plaatje0"

# Uitleg box
text='''Vul eigen waardes in, 
klik dan op: Bereken.

Of

Selecteer een plaatje, klik dan: 
plaats de gekozen plaatje en dan 
Bereken.'''
    
Uitleg = Text(scherm, height=8, width=35)
Uitleg.insert('end', text)
Uitleg.config(state='disabled')
Uitleg.place(x=360,y=13)

# Afbeelding van Mandelbrot; hier ken je de variabel afbeelding toe aan de Mandelbrot afbeelding
afbeelding = Label(scherm); afbeelding.place(x=10,y=140)

# Aantal pixels in de x en y richting van Mandelbrot
width_x, height_y = 400, 400

# Toepassen van de formule en condities Mandelbrot
def calc(x, y):
    a = 0; b = 0; mandelgetal = 0; pythagoras = 0
    while pythagoras <= 2 and mandelgetal <= maxIt: # Afstand niet groter dan 2 en functie stopt als het bij de aangegeven max. iteraties komt
        pythagoras = math.sqrt(a*a + b*b) # Berekenen de afstand
        a, b = a*a - b*b + x, 2*a*b + y # Formule van de Mandelbrot
        mandelgetal += 1 # Het mandelgetal telt hoevaak de functie is toegepast
        
    if mandelgetal == 1: # Conditie als het mandelgetal al 1 is dan geeft hij gelijk 1 terug
         return 1
    elif mandelgetal == maxIt: # Conditie als mandelgetal oneindig is dan stoppen we met het toepassen van de functie en zetten we het mandelgetal op max iteraites
        return maxIt
    else:
        return mandelgetal # Als het mandelgetal niet gelijk is aan de vorige condities
                           # dan is het mandelgetal tussen 1 en maxIt


# Declaratie globale variabelen van de kleurslider
Red = 0; Green = 0; Blue = 0

def slider_value():
    global Red, Green, Blue
    try:
        Red = sliderRed.get() # Leest de Rode slider
        Green = sliderGreen.get()
        Blue = sliderBlue.get()
        teken() # Gelezen kleur wordt toegepast in de Mandelbrot
    except:
        Red = 0 # Integers
        Green = 0 
        Blue = 0
        teken()

def teken():
    plaatje = Image.new(mode="RGB", size=(width_x,height_y)) 
    draw = Draw(plaatje)
    
    for row in range(width_x): # De row stopt als het bij 400 komt in x-richting
        x = (row-200) * schaal + CoordinaatX # Verandert naar wat we willen zien van de Mandelbrot. En gaat naar het midden in de x-richting
        for col in range(height_y): # Stopt bij 400 maar nu in y-richting
            y = (col-200) * schaal - CoordinaatY # Gaat naar het midden maar nu in de y-richting. Daar kunnen we schalen en coordinaten aanpassen
            
            v = calc(x,y) # Roept de Mandelbrot op, maar krijgt Mandelgetal terug
            if(v % 2 != 0): # Als conditie waar is dan krijg je een zwarte pixel en zo niet een wit pixel
                plaatje.putpixel((row, col), (0 , 0, 0)) # Set pixel op zwart
            else:
                plaatje.putpixel((row, col), (255 , 255, 255)) # Set pixel op wit
                R = 125 + Red # Rood 
                G = 125 + Green*v # Groen
                B = 125 + int(v * Blue / 8) # Blauw
                plaatje.putpixel((row, col),(R, G, B))  

    global omgezetPlaatje
    omgezetPlaatje = PhotoImage(plaatje)
    afbeelding.configure(image=omgezetPlaatje)  

# Declaratie van globale variables
CoordinaatX = 0; CoordinaatY = 0; schaal = 0; maxIt = 0

# functie vraagt de input van de gebruiker en pas ze toe in de functie teken()
def bereken(): 
    global CoordinaatX, CoordinaatY, schaal, maxIt # Alle variabelen die worden gebruikt worden global in plaats van local variables,
    try:                                           # want we willen de coordinaten, schaal en aantal iteraties kunnen veranderen
        CoordinaatX = float(InvoerMiddenX.get()) # Vraagt de input InvoerMiddenx en maakt het een float van
        CoordinaatY= float(InvoerMiddenY.get())
        schaal=float(InvoerSchaal.get())
        maxIt=int(InvoerIteraties.get())
        teken()
    except:
        CoordinaatX = 0.0 # Dit is een float
        CoordinaatY= 0.0
        schaal= 0.00
        maxIt= 0 # Dit is een integer
        teken()

# Setup van de sliders
tekst = Label(scherm, text="Kleur aanpas slider", font='Arial 18 bold'); tekst.place(x=420, y=260);

# Slider van de eerste slider met naam Red
tekst = Label(scherm, text="Red", font=("Arial", 18)); tekst.place(x=530, y=315);
sliderRed = Scale(scherm, from_ = 0, to=100, orient=HORIZONTAL)
sliderRed.place(x=420,y=300)

# Green
tekst = Label(scherm, text="Green", font=("Arial", 18)); tekst.place(x=530, y=355);
sliderGreen = Scale(scherm, from_ = 0, to=100, orient=HORIZONTAL)
sliderGreen.place(x=420,y=340)

# Blauw
tekst = Label(scherm, text="Blue Hue", font=("Arial", 18)); tekst.place(x=530, y=395);
sliderBlue = Scale(scherm, from_ = 0, to=100, orient=HORIZONTAL)
sliderBlue.place(x=420,y=380)

def left(event): # Functie voor linkermuisklik 
    global CoordinaatX, CoordinaatY, schaal 
    pointxy = (event.x, event.y) # Opvragen van de positie van de muis
    
    CoordinaatX = (pointxy[0] - 200) * schaal  #Het vervangen van de coordinaten met de x-coordinaten van de muis
    
    InvoerMiddenX.delete(0, "end") # Verwijderen van vorige invoer
    InvoerMiddenX.insert(0,str(CoordinaatX)) # Invullen van de invoer met de x-coordinaten van de muis
    
    CoordinaatY = (200 - pointxy[1]) * schaal # Veranderen van de y-coordinaat
    
    InvoerMiddenY.delete(0, "end")
    InvoerMiddenY.insert(0, str(CoordinaatY))
    
    schaal /= 1.5 #Schaalvergroting
    InvoerSchaal.delete(0,"end")
    InvoerSchaal.insert(0, str(schaal))
    teken() # Toepassen op de Mandelbrot afbeelding
    
def right(event): # Definitie voor rechtermuisklik
    global CoordinaatX, CoordinaatY, schaal
    pointxy = (event.x, event.y)
    
    CoordinaatX = (pointxy[0] - 200) * schaal
    
    InvoerMiddenX.delete(0, "end")
    InvoerMiddenX.insert(0,str(CoordinaatX)) 
    
    CoordinaatY = (200 - pointxy[1]) * schaal
    
    InvoerMiddenY.delete(0, "end")
    InvoerMiddenY.insert(0, str(CoordinaatY))

    schaal *= 1.5 # Schaalverkleining
    InvoerSchaal.delete(0,"end")
    InvoerSchaal.insert(0, str(schaal))
    teken()

afbeelding.bind('<Button-1>', left) # Linkermuisklik activeert functie left()
afbeelding.bind('<Button-2>', right) # Rechtermuisklik activeert functie right()

# Knop voor het aanpassen van kleur
kleurknop = Button(scherm, text="Verander kleur", font=("Arial, 18"), height=1,width=10); kleurknop.place(x=420,y=440); 
kleurknop.configure(command=slider_value) # Het verkrijgen de slidervalue

# Setup lijst van de keuze plaatjes
drop = OptionMenu(scherm, clicked, *options); drop.place(x=420, y=140)
myButton = Button(scherm, text="Plaats de gekozen plaatje",command=keuze); myButton.place(x=417, y=165)

knop.configure(command=bereken) # Knop voor de functie "bereken" die de input van de gebruiker toepast
bereken() # Activeert de functie voor het tekenen van de Mandelbrot voor de eerste keer

scherm.mainloop()
