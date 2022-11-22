#python3.11 -m venv "virtual omgeving"
#source studysession/bin/activate
#pip3 install matplotlib

#Zilon Huang & Joran Middelman

from tkinter import *
import math

#initialise the window
scherm = Tk()
scherm.geometry("600x150")
scherm.title("Mandelbrot")

#setup of midden x:
tekst = Label(scherm)
tekst.place(x=10, y=10)
tekst.configure(text="midden x:")

mx = invoer = Entry(scherm)
invoer.place(x=100, y=10)
invoer.configure(width=10)

#setup of midden y:
tekst = Label(scherm)
tekst.place(x=10, y=40)
tekst.configure(text="midden y:")

my = invoer = Entry(scherm)
invoer.place(x=100, y=40)
invoer.configure(width=10)

#setup of schaal:
tekst = Label(scherm)
tekst.place(x=10, y=70)
tekst.configure(text="schaal:")

s = invoer = Entry(scherm)
invoer.place(x=100, y=70)
invoer.configure(width=10)

#setup of iterations:
tekst = Label(scherm)
tekst.place(x=10, y=100)
tekst.configure(text="iteraties:")

i = invoer = Entry(scherm)
invoer.place(x=100, y=100)
invoer.configure(width=3)

#setup van de knop
knop = Button(scherm)
knop.place(x=140,y=100)
knop.configure(text="Bereken")

#tekenen van mandelbrot

#Mandelbrot algorithm

scherm.mainloop()