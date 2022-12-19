#Todo: game mechanics, thats it --> Oplossen hoe we die schijven kunnen onderscheiden van elkaar. 

# import libraries
from tkinter import *

# setup van scherm
scherm = Tk()
scherm.title("Reversi")
c = Canvas(scherm, width=475,height=271)
c.pack()

# declaratie van variabelen
vierhoek_size = 45
speel_bord = 6
marge_tussen_lijn_en_schijf = 4
teller = 0

# Initialise het speelbord
def Begin_Bord():
    board = {}
    for i in range(0, speel_bord):
        board[i] = {}
        for j in range(0, speel_bord):
            board[i][j] = 0
    return board

# Declareren van de speelbord
board = Begin_Bord()

# Begin stand van het bord
def begin_stand_bord():
    for i in range(speel_bord):
        for j in range(speel_bord):
            Boord_Spel_Kleur = "#007500" # Hexadecimal value for dark green
            x0 = i * vierhoek_size + 3 # plaats van het bord op scherm
            y0 = j * vierhoek_size + 3 # "+ 3" is een cosmetisch correctie 
            c.create_rectangle(x0, y0, x0 + vierhoek_size, y0 + vierhoek_size, fill = Boord_Spel_Kleur, width=1) # plaatsen van het speelvlak met vierhoek_size als grootte
            
begin_stand_bord()

# Plaatst schijven voor begin spel
def schijf_start():        
    for x in range(2,4):
        for y in range(2,4):
            if x==2 and y==2 or x==3 and y==3: # plaats op board[i][j] die ingevuld moetenworden
                board[x][y] = c.create_oval(x * vierhoek_size + marge_tussen_lijn_en_schijf, 
                                          y * vierhoek_size + marge_tussen_lijn_en_schijf, 
                                          x * vierhoek_size + vierhoek_size + 1, 
                                          y * vierhoek_size + vierhoek_size + 1, fill = "#000000", width=0) # witte schijf
            else: 
                board[x][y] = c.create_oval(x * vierhoek_size + marge_tussen_lijn_en_schijf, 
                                          y * vierhoek_size + marge_tussen_lijn_en_schijf, 
                                          x * vierhoek_size + vierhoek_size + 1, 
                                          y * vierhoek_size + vierhoek_size + 1, fill = "#ffffff", width=0) # zwart schijf

schijf_start()

# Plaatsen van zwarte en witte schijven
def plaats_schijf(event): 
    global teller
    # opvragen coordinaten 
    x = event.x - 4 # correctie van beginstand bord en wat meer
    y = event.y - 4
    # Omzetten naar integers om de schijven in het vak te kunnen plaatsen
    x0 = int(x / vierhoek_size)
    y0 = int(y / vierhoek_size)
    # print(f"{x0},{y0}")

    # functie checkt of de speler aan de beurt is en ook op het speelbord klikt zo ja plaatst die een schijf
    if(isOnBoard(x0,y0) == True and teller%2==0):
            board[x0][y0] = c.create_oval(x0 * vierhoek_size + marge_tussen_lijn_en_schijf, 
                          y0 * vierhoek_size + marge_tussen_lijn_en_schijf, 
                          x0 * vierhoek_size + vierhoek_size + 1, 
                          y0 * vierhoek_size + vierhoek_size + 1, fill = "#000000", width=0, tags=("cicles",))


    if(isOnBoard(x0,y0) == True and teller%2 != 0):
            board[x0][y0] = c.create_oval(x0 * vierhoek_size + marge_tussen_lijn_en_schijf, 
                              y0 * vierhoek_size + marge_tussen_lijn_en_schijf, 
                              x0 * vierhoek_size + vierhoek_size + 1, 
                              y0 * vierhoek_size + vierhoek_size + 1, fill = "#ffffff", width=0, tags=("cicles",))
            # tekst = Label(scherm, text="zwart is aan de beurt", font=("Arial", 18)); tekst.place(x=300, y=100);
    teller += 1

# checkt of het een geldige zet is binnen het bord
def isOnBoard(x, y):
    if x >= 0 and x <= speel_bord - 1 and y >= 0 and y <= speel_bord - 1:
        return True
    else:
        return False
            
scherm.bind("<Button-1>", plaats_schijf) # Als de gebruiker op de scherm klikt krijg je coordinaten in i en j
            
def reset():
    for _ in range(0, vierhoek_size):
        for _ in range(0, vierhoek_size):
            find_cicles = c.find_withtag("cicles")
            c.delete(find_cicles[0])
            schijf_start()

def countTile(board, tile):
    stones = 0
    for i in range(0, speel_bord):
        for j in range(0, speel_bord):
            if board[i][j] == tile:
                stones += 1
    print(stones)
    return stones

HelpButton = Button(scherm, text="Help", height=1,width=5); HelpButton.place(x=280,y=5)
NieuwSpel = Button(scherm, text="Nieuw Spel", height=1,width=6); NieuwSpel.place(x=380, y=5); NieuwSpel.configure(command=reset)

scherm.mainloop()
