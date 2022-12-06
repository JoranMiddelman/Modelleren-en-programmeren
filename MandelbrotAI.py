#Zilon Huang & Joran Middelman

#import benodigde libraries
from tkinter import *
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage 
from PIL import Image
import math

#initialise the window
scherm = Frame()
scherm.master.title("Mandelbrot")
scherm.configure(width=620,height=550)
scherm.pack()

#setup of midden x:
tekst = Label(scherm, text="Midden x:", font=("Arial", 18)); tekst.place(x=10, y=10);
InvoerMiddenX  = Entry(scherm, width=10); InvoerMiddenX.place(x=100, y=10); InvoerMiddenX.insert(0,str(0));

#setup of midden y:
tekst = Label(scherm, text="midden y:", font=("Arial", 18)); tekst.place(x=10, y=40);
InvoerMiddenY = Entry(scherm, width=10); InvoerMiddenY.place(x=100, y=40); InvoerMiddenY.insert(0,str(0));

#setup of schaal:
tekst = Label(scherm, text="schaal:", font=("Arial", 18)); tekst.place(x=10, y=70);
InvoerSchaal = Entry(scherm, width=10); InvoerSchaal.place(x=100, y=70); InvoerSchaal.insert(0,str(1e-2));

#setup of iterations:
tekst = Label(scherm, text="iteraties:", font=("Arial", 18)); tekst.place(x=10, y=100);
InvoerIteraties = Entry(scherm, width=10); InvoerIteraties.place(x=100, y=100); InvoerIteraties.insert(0,str(100));

#setup van de knop
knop = Button(scherm, text="Bereken", font=("Arial, 18"), height=5,width=10); knop.place(x=210,y=10);

#setup van de keuze menu van vooraf bepaalde plaatjes
def keuze():
    a = clicked.get() 
    if a == options[0]:
        InvoerMiddenX.delete(0, 'end') # verwijderd de input van de vorige invoer
        InvoerMiddenY.delete(0, 'end')
        InvoerIteraties.delete(0, 'end')
        InvoerSchaal.delete(0, 'end')

        InvoerMiddenX.insert(0,str(-0.40)) # kent de waarde toe aan de entry 
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
    elif a == options[2]:
        InvoerMiddenX.delete(0, 'end')
        InvoerMiddenY.delete(0, 'end')
        InvoerIteraties.delete(0, 'end')
        InvoerSchaal.delete(0, 'end')

        InvoerMiddenX.insert(0,str(-0.2))
        InvoerMiddenY.insert(0,str(-0.65))
        InvoerIteraties.insert(0,str(400))
        InvoerSchaal.insert(0,str(1e-5))
    
options = [ 
           "Plaatje0",
           "Plaatje1",
           "Plaatje2"
]

clicked = StringVar()
clicked.set("Selecteer een plaatje")

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
    if mandelgetal == maxIt: # Conditie als mandelgetal oneindig is dan stoppen we met het toepassen van de functie en zetten we het mandelgetal op max iteraites
        return maxIt
    else:
        return mandelgetal # Als de vorige niet voordoen dan is het mandelgetal tussen 1 en maxIt


# Declaratie globale variabelen van de kleuren met slider
Red = 0; Green = 0; Blue = 0

def slider_value():
    global Red, Green, Blue
    try:
        Red = sliderRed.get()
        Green = sliderGreen.get()
        Blue = sliderBlue.get()
        teken()
    except:
        Red = 0
        Green = 0 
        Blue = 0
        teken()

def teken():
    plaatje = Image.new(mode="RGB", size=(width_x,height_y))
    draw = Draw(plaatje)
    
    for row in range(width_x):
        x = (row-200) * schaal + CoordinaatX
        for col in range(height_y):
            y = (col-200) * schaal - CoordinaatY
            
            v = calc(x,y)
            if(v % 2 != 0):
                plaatje.putpixel((row, col), (0 , 0, 0))
            else:
                plaatje.putpixel((row, col), (255 , 255, 255))
                hue = int(v * 255 / maxIt)
                saturation = int(Red * 255 / maxIt)
                value = Blue if v < maxIt else 0
                plaatje.putpixel((row, col),(hue, saturation, value))  

    global omgezetPlaatje
    omgezetPlaatje = PhotoImage(plaatje)
    afbeelding.configure(image=omgezetPlaatje)  

# Declaratie van globale variables
CoordinaatX = 0; CoordinaatY = 0; schaal = 0; maxIt = 0

# functie vraagt de input van de gebruiker en pas ze toe in de functie teken()
def bereken(): 
    global CoordinaatX, CoordinaatY, schaal, maxIt
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

tekst = Label(scherm, text="Kleur aanpas slider", font='Arial 18 bold'); tekst.place(x=420, y=260);

tekst = Label(scherm, text="Red", font=("Arial", 18)); tekst.place(x=530, y=315);
sliderRed = Scale(scherm, from_ = 0, to=255, orient=HORIZONTAL)
sliderRed.place(x=420,y=300)

tekst = Label(scherm, text="Green", font=("Arial", 18)); tekst.place(x=530, y=355);
sliderGreen = Scale(scherm, from_ = 0, to=255, orient=HORIZONTAL)
sliderGreen.place(x=420,y=340)

tekst = Label(scherm, text="Blue", font=("Arial", 18)); tekst.place(x=530, y=395);
sliderBlue = Scale(scherm, from_ = 0, to=255, orient=HORIZONTAL)
sliderBlue.place(x=420,y=380)

def left(event): #Definitie voor een linkermuisklik 
    global CoordinaatX; global CoordinaatY; global schaal
    pointxy = (event.x, event.y) # Opvragen van de positie van de muis
    print(pointxy)
    
    CoordinaatX = (pointxy[0] - 200) * schaal  #Het vervangen van de coordinaten met de coordinaten van de muis
    
    InvoerMiddenX.delete(0, "end") # Verwijderen van vorige invoer
    InvoerMiddenX.insert(0,str(CoordinaatX)) # Invullen van de coordinaten met de muisgeklikt
    
    CoordinaatY = (pointxy[1] - 200) * schaal # Verandert de beeld van mandelbrot 
    
    InvoerMiddenY.delete(0, "end")
    InvoerMiddenY.insert(0, str(CoordinaatY))
    
    schaal /= 1.5 #Schaalvergroting
    InvoerSchaal.delete(0,"end")
    InvoerSchaal.insert(0, str(schaal))
    teken()
    
def right(event): # Definitie voor rechtermuisklik
    global x; global y; global schaal
    pointxy = (event.x, event.y)
    print(pointxy)
    
    CoordinaatX = (pointxy[0] - 200) * schaal
    
    InvoerMiddenX.delete(0, "end")
    InvoerMiddenX.insert(0,str(CoordinaatX)) 
    
    CoordinaatY = (pointxy[1] - 200) * schaal
    
    InvoerMiddenY.delete(0, "end")
    InvoerMiddenY.insert(0, str(CoordinaatY))

    schaal *= 1.5 # Schaalverkleining
    InvoerSchaal.delete(0,"end")
    InvoerSchaal.insert(0, str(schaal))
    teken()

afbeelding.bind('<Button-1>', left) # linkermuisklik leidt tot activatie van functie left()
afbeelding.bind('<Button-2>', right) #Doet iets als rechtermuisklik wordt geactiveerd

# knop voor aanpassen kleur
kleurknop = Button(scherm, text="Verander kleur", font=("Arial, 18"), height=1,width=10); kleurknop.place(x=420,y=440); 
kleurknop.configure(command=slider_value) # Het verkrijgen van de waarde van de sliders

# lijst van de keuze plaatjes
drop = OptionMenu(scherm, clicked, *options); drop.place(x=420, y=140)
myButton = Button(scherm, text="Plaats de gekozen plaatje",command=keuze); myButton.place(x=417, y=165) # knop voor kiezen plaatje

knop.configure(command=bereken) # Knop bereken doet iets als het wordt ingedrukt
bereken() # activeert de functie voor het tekenen van de mandelbrot voor de eerste keer

scherm.mainloop()
