#Zilon Huang & Joran Middelman

# Import libraries
from tkinter import Tk, Canvas, StringVar, OptionMenu, Button
import numpy as np 

# Setup van scherm met de canvas erop
scherm = Tk()
scherm.title("Reversi")
c = Canvas(scherm, width = 730, height = 501)
c.pack()

# Declaratie van speelbord grootte
speelbord = 10

def board():
    board = np.zeros((speelbord, speelbord)) # Gebruik van numpy library, omdat het makkelijker is. De opdracht maakt een 'n x n' matrix gevuld met 0 als basis
    
    # Plaatsen van de vier schijven voor begin van het spel. De stand van het bord
    board[int(speelbord / 2) - 1][int(speelbord / 2) - 1] = 1 # Wit schijf
    board[int(speelbord / 2)]    [int(speelbord / 2)] =     1 # Toekenningsopdracht welk board je wil aanpassen en dan vervolgens de plaatsnummers in de matrix [i, j]
    board[int(speelbord / 2) - 1][int(speelbord / 2)] =     2 # Zwart schijf
    board[int(speelbord / 2)]    [int(speelbord / 2) - 1] = 2

    return board # Krijg de beginsituatie van het bord 

board = board() # Aanroepen van de functie om de board variabele te kunnen gebruiken

# Grootte van de vierkanten
vierhoek_size = 50

# Schijf in de vierkanthok plaatsen. Correctie zodat het past
marge_lijn_schijf = 6 

# Kleine cirkeltjes voor de mogelijke zetten
midden_vierhoek = 22
circle_size = 35

# Kleur de schijven
kleur_zwart = "#000000" # Hexadecimal value voor zwart
kleur_wit = "#ffffff" # Hexadecimal value voor wit

# Score declaratie 
wit_score = 0
zwart_score = 0

# Toekenning van nummers aan naam
wit_speler = 1
zwart_speler = 2

#Huidige speler declaratie
huidige_speler = zwart_speler

# Teller voor wie aan de beurt is
teller = 0

# Declaratie boolean variabele
help = True

# Methode voor beginstand bord
def basis_spel_bord(board):
    for i in range(speelbord): # Loop voor het aantal vierkanten dat geplaatst moet worden in rijen en kolommen
        for j in range(speelbord):
            Boord_Kleur = "#007500" # Hexadecimal value voor donker groen. Speelbord kleur
            x_bord = i * vierhoek_size + 3 # Coordinaten waar de vierkant geplaatst moet worden met grootte vier_hoek_size
            y_bord = j * vierhoek_size + 3 # waarbij "+ 3" een cosmetisch correctie is
            c.create_rectangle(x_bord, 
                               y_bord, 
                               x_bord + vierhoek_size, 
                               y_bord + vierhoek_size, 
                               fill = Boord_Kleur, width=1, tags = "bord") # Tekent de bord waarop we Reversi gaan spelen
            # Plaatst de witte en zwarte schijven in het vak
            if board[i,j] == wit_speler: # Witte schijf is verbonden met integer: 1
                c.create_oval(i * vierhoek_size + marge_lijn_schijf, # Tekent witte schijf op bord
                              j * vierhoek_size + marge_lijn_schijf, 
                              i * vierhoek_size + vierhoek_size, 
                              j * vierhoek_size + vierhoek_size, 
                              fill = kleur_wit, width=0, tags = "reset")
            elif board[i,j] == zwart_speler: # Zwarte schijf is verbonden met integer: 2
                c.create_oval(i * vierhoek_size + marge_lijn_schijf, # Tekent zwarte schijf
                              j * vierhoek_size + marge_lijn_schijf, 
                              i * vierhoek_size + vierhoek_size, 
                              j * vierhoek_size + vierhoek_size, 
                              fill = kleur_zwart, width=0, tags = "reset")
    find_all_valid_moves() # Om de mogelijke zetten te tonen moet de functie worden opgeroepen wanneer het spel start of het speelvlak update
    get_score() # De score updaten als basis_speel_bord functie wordt aangeroepen

# Functie als speler zwart aan de beurt is dan krijg je wit terug als integer and vice versa
def opposite(player: int):
    return zwart_speler if player == wit_speler else wit_speler     

def Muisklik(event):
    # Declaratie van muiscoordinaten die global moeten zijn
    global x0, y0
    # Opvragen muiscoordinaten na linkermuisklik
    muis_x, muis_y = event.x - 4, event.y - 4 # "- 4" is een correctie, zodat muisklik daadwerkelijk overeenkomt met het vierkantje
    # Omzetten naar integers om de schijven in het gekozen vierkantje te plaatsen
    x0, y0 = int(muis_x / vierhoek_size), int(muis_y / vierhoek_size)
    
    # Bijhouden wie er aan de beurt is en in global zodat de stand ervan niet word verwijdert
    global teller, huidige_speler 
    if (x0, y0) in valid_moves: # Alleen als het een geldige klik was en niet een random muisklik op speelbord dan is de volgende aan de beurt
        if teller == 0: # Als de teller weer gelijk is aan 0 is aan wit_speler de beurt
          huidige_speler = wit_speler
        else: # Als teller niet gelijk is aan 0, maar in dit geval 1 is dan is zwart aan de beurt
          huidige_speler = zwart_speler
        teller += 1 # Increment als beurt is geweest
        teller %= 2 # Opdracht laat teller alleen getallen tussen 0 en 1 toe
    
    schijf() # Roept de volgende functie op om de muisklik coordinaten die zijn opgeslagen te gebruiken
      
def schijf():        
    # Voorwaarde (x0, y0) op bord, met de waarde 0. Die in een array zit van geldige zetten
    if board[x0, y0] == 0 and (x0, y0) in valid_moves: # Voordat er schijven geplaatst kunnen worden moet de zet in de lijst van geldige zetten zitten
        board[x0, y0] = huidige_speler # De plaats waarop wordt geklikt is de zet van de huidige speler
        # for d in directions:
        for dx in range(-1,2): # Zoeken in de 8 richtingen rondom de schijf
            for dy in range(-1,2):
                x = x0
                y = y0
                while dx != 0 or dy !=0: # Coordinaat (0, 0) mag niet voorkomen
                    x = x + dx # Voeg dx toe aan de coordinaat van de huidige muisklik
                    y = y + dy # Doe dat ook voor y variabele
                    if op_speel_vlak(x, y): # Check of we nog op het speelbord zijn
                        if board[x, y] == 0: # Er is niks te checken als het naast gelegen vak geen schijf bevat
                            break
                        if huidige_speler == board[x, y]: # Vind de schijven van dezelfde speler op de bord
                            i, j = x0, y0
                            while i != x or j != y: # Gaat door totdat we bij de andere schijf zijn van de speler
                                i, j = i + dx, j + dy # De muisklik coordinaten tot de andere schijf van de speler
                                board[i, j] = huidige_speler # Veranderd de gevonden schijven tussen twee schijven vandezelfde keur in de huidige spelers kleur
                    else:
                        break # Als het zoeken niet op het speelvlak bevind dan gaat hij uit de loop
        basis_spel_bord(board) # Updaten van het speelvlak nieuwe schijven
        find_all_valid_moves() # Zoeken naar gelidge zetten

def op_speel_vlak(x, y): # Muisklik coordinaten controleren of ze op het speelvlak bevinden
    if 0 <= x <= speelbord - 1 and 0 <= y <= speelbord - 1: # Telling bij computers begint met 0 dus moet "- 1" als correctie
        return True # Als het op het speelvlak is dan boolean True
    else: 
        return False # Anders False
                    
def check_possible_positions(x,y):
    if op_speel_vlak(x, y) and board[x,y] == 0: # Checkt of schijf op het speelvlak is en de gekozen vak niet al een schijf bevat
        for dx in range(-1,2): # Zoeken in de 8 richtingen rondom de schijf
            for dy in range(-1,2):
                if dx != 0 or dy !=0: # Mag geen coordinaat (0, 0) zijn
                    nieuw_x, nieuw_y = x + dx, y + dy # Verschuiven naar rondom de gekozen coordinaten
                    if op_speel_vlak(nieuw_x, nieuw_y) and board[nieuw_x, nieuw_y] == huidige_speler: # De verschuiving moet op de speelbord blijven en de hetzelfde zijn als de huidige speler
                        while op_speel_vlak(nieuw_x, nieuw_y) and board[nieuw_x, nieuw_y] == huidige_speler: # Blijf in deze richting doorzoeken
                            nieuw_x, nieuw_y = nieuw_x + dx, nieuw_y + dy
                        if op_speel_vlak(nieuw_x, nieuw_y) and board[nieuw_x, nieuw_y] == opposite(huidige_speler): # Het is een gelidge zet als de zet naast de schijf is van de tegenstander waardoor we de tegenstanders schijf insluiten
                            return True 
        return False
    else:
        return False # Als het niet op het speelvlak is en het vak al bezet is door een schijf
    
def find_all_valid_moves():
    global valid_moves # Declaratie van variabele die in andere functies word gebruikt
    valid_moves = [] # Vind alle mogelijke zetten. Als gevonden plaats in een lijst
    for i in range(speelbord): # Doe dat voor alle vakken op het speelvlak
        for j in range(speelbord):
            if check_possible_positions(i,j): # Vind de mogelijke zetten
                valid_moves.append((i,j)) # Voeg ze toe in de lijst
                if board[i,j] == 0 and help == True: # Plaats de kleine hulp cirkels op speelvlak als speelvlak geen schijf bevat, en de knop help is ingeschakeld
                    c.create_oval(i * vierhoek_size + midden_vierhoek,   
                                j * vierhoek_size + midden_vierhoek, 
                                i * vierhoek_size + circle_size, 
                                j * vierhoek_size + circle_size, 
                                outline= "black", 
                                width=2, tags = "help")
                elif help == False:
                    c.delete("help") # Het verweideren van de hulp cirkels als de hulp knop is geklikt

def get_score():
    wit_score = 0
    zwart_score = 0
    # Zoeken naar witte en zwarte schijven op bord indien gevonden increment met 1
    for i in range(speelbord):
        for j in range(speelbord):
            if board[i,j] == wit_speler:
                wit_score += 1
            if board[i,j] == zwart_speler:
                zwart_score += 1
                
    # Als de grootte van de lijst van geldige zetten gelijk is aan nul dan is het spel klaar en kan dus een conclusie worden getrokken
    if len(valid_moves) == 0:
        if wit_score > zwart_score:
            c.create_text(140 + speelbord * vierhoek_size, 380, text="Wit heeft gewonnen!", tags="reset")
            c.create_oval(5 + speelbord * vierhoek_size, 355, 
                        55 + speelbord * vierhoek_size, 405, fill = kleur_wit, width=0, tags="reset")
        elif wit_score == zwart_score:
            c.create_text(100 + speelbord * vierhoek_size, 380, text="Gelijkspel!", tags="reset")
            c.create_oval(145 + speelbord * vierhoek_size, 355, 
                        195 + speelbord * vierhoek_size, 405, fill = kleur_wit, width=0, tags="reset")
            c.create_oval(5 + speelbord * vierhoek_size, 355, 
                        55 + speelbord * vierhoek_size, 405, fill = kleur_zwart, width=0, tags="reset")
        else:
            c.create_text(140 + speelbord * vierhoek_size, 380, text="Zwart heeft gewonnen!", tags="reset")  
            c.create_oval(5 + speelbord * vierhoek_size, 355, 
                        55 + speelbord * vierhoek_size, 405, fill = kleur_zwart, width=0, tags="reset")
             
    # Wie is er aan de beurt op scherm tonen     
    if teller == 0:
        c.delete("beurt")
        c.create_text(150 + speelbord * vierhoek_size, 155, text="Beurt: Wit", tags="beurt")
        c.create_oval(50 + speelbord * vierhoek_size, 130, 
                      100 + speelbord * vierhoek_size, 180, fill = kleur_wit, width=0, tags="beurt")
    else: 
        c.delete("beurt")
        c.create_text(150 + speelbord * vierhoek_size, 155, text="Beurt: Zwart", tags="beurt")
        c.create_oval(50 + speelbord * vierhoek_size, 130, 
                      100 + speelbord * vierhoek_size, 180, fill = kleur_zwart, width=0, tags="beurt")
        
    # Zwarte en witte schijf op scherm voor de scoreboard
    c.create_oval(6 + speelbord * vierhoek_size, 3, 56 + speelbord * vierhoek_size, 53, fill = kleur_zwart, width=0, tags="Score_bord")
    c.create_oval(6 + speelbord * vierhoek_size, 56, 56 + speelbord * vierhoek_size, 106, fill = kleur_wit, width=0, tags="Score_bord")
                
    # Verweideren van outdated score
    c.delete("score")
    
    # Plaats de score voor witte en zwarte schijf op scherm
    c.create_text(130 + speelbord * vierhoek_size, 30, text="Score voor zwart is: %s"%zwart_score, tags="score")
    c.create_text(130 + speelbord * vierhoek_size, 80, text="Score voor wit is: %s"%wit_score, tags="score")

# Scherm grootte veranderen naar de juiste formaat
def Resize():
    if a == options[0]: # 4 x 4. Als keuze van het menu gelijk is aan de eerste in de lijst van keuze's
        scherm.geometry("415x408") # dan moet het scherm formaat gelijk zijn aan "415x310"
    elif a == options[1]:
        scherm.geometry("515x408") # 6 x 6
    elif a == options[2]:
        scherm.geometry("616x408") # 8 x 8
    elif a == options[3]:
        scherm.geometry("730x508") # 10 x 10

# Aanpassen van de speelbord grootte
def keuze_afmeting_speelbord():
    global speelbord, a # Global variabele om de scherm daadwerkelijk te kunnen veranderen, met daarbij de screen resize 
    a = clicked.get() # Het omzetten van de keuze in een bruikbare variabele
    if a == options[0]: # Als de eerste keuze in de lijst wordt gekozen
        speelbord = 4# dan wordt de grootte een "4 x 4" speelbord
        Resize()
    elif a == options[1]:
        speelbord = 6
        Resize()
    elif a == options[2]:
        speelbord = 8
        Resize()
    elif a == options[3]:
        speelbord = 10
        Resize()
        
    # De help/Nieuwe spel knoppen en de menu een plaats geven en in de functie zodat het mee verandert met de speelbord grootte 
    option_menu.place(x = 7 + speelbord * vierhoek_size, y=255)
    Button_voor_keuze_afmeting_speelbord.place(x = 4 + speelbord * vierhoek_size, y = 278)
    Nieuw_spel_Button.place(x = 30 + speelbord * vierhoek_size, y = 200)
    Help_Button.place(x = 150 + speelbord * vierhoek_size, y = 200)
    
    Nieuw_spel() # Roept functie op om de speelbord schoon te vegen en een nieuwe spel te starten

# Dit zijn de opties die in het menu worden gegeven
options = ["4 x 4", 
           "6 x 6", 
           "8 x 8", 
           "10 x 10"
]

clicked = StringVar() # Opslaan van de keuze in het menu
clicked.set("Selecteer afmeting speelbord") # Tekst als de menu nog niet is gebruikt

# Maken van menu
option_menu = OptionMenu(c, clicked, *options); option_menu.place(x = 7 + speelbord * vierhoek_size, y=255)

# Maken van de "Bevestig keuze speelbord" knop
Button_voor_keuze_afmeting_speelbord = Button(c, text = "Bevestig keuze speelbord", command = keuze_afmeting_speelbord)
Button_voor_keuze_afmeting_speelbord.place(x = 4 + speelbord * vierhoek_size, y = 278)

def Nieuw_spel():
    # Schoon vegen van het speelvlak. Als op bord een getal groter is dan 0 dan verandert dat dan naar een 0
    board[board > 0] = 0
    # Plaats de begin stand bord
    board[int(speelbord / 2) - 1][int(speelbord / 2) - 1] = 1 # Wit schijf
    board[int(speelbord / 2)]    [int(speelbord / 2)] =     1
    board[int(speelbord / 2) - 1][int(speelbord / 2)] =     2 # Zwart schijf
    board[int(speelbord / 2)]    [int(speelbord / 2) - 1] = 2
    
    # Verwijder alle gegevens van de vorige spel
    c.delete("bord")
    c.delete("help")
    c.delete("reset")
    c.delete("Score_bord")
    
    basis_spel_bord(board) # Reset de bord met de aanpassingen

def help_knop(): # Het aan- en uitzetten van de help knop 
    global help # Omdat het een globale variabele is wordt de vorige stand opgeslagen en dus niet verwijdert voor de volgende aanroep
    if help == True:
        help = False 
    elif help == False:
        help= True
    find_all_valid_moves() # Het aan en uit kunnen zetten van de help cirkels

# Het aanmaken van de Nieuwe spel knop en Help knop
Nieuw_spel_Button = Button(c, text="Nieuwe spel", command = Nieuw_spel); Nieuw_spel_Button.place(x = 30 + speelbord * vierhoek_size, y = 200)
Help_Button = Button(c, text="Help", command = help_knop); Help_Button.place(x = 150 + speelbord * vierhoek_size, y = 200)

# Roept voor het begin van programma het speelvlak op 
Nieuw_spel()

# Linkermuisklik zorgt ervoor dat de functie Muisklik wordt aangeroepen
c.bind('<Button-1>', Muisklik)

scherm.mainloop()
