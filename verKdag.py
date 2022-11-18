#Zilon Huang & Joran Middelman

#import van library
from datetime import datetime, date, timedelta

#vraag om de geboorte datum - user input
Verjaardag = input("Geef je geboortedatum in dag/maand/jaar: ")

#verkregen verjaardag. Onnodige informatie zoals tijd weghalen
dataVerjaardag = datetime.strptime(Verjaardag, '%d/%m/%Y').date()

#verkrijgen van de datum heden
dataNu = datetime.date(datetime.now())

#hoeveel dagen leeft iemand
data_verschil = (dataNu - dataVerjaardag).days

#andere naam geven
a = data_verschil

#resten berekenen
x = (a % 1000)

#tellen hoeveel dagen tot de volgende verKdag
count = 0

while (x < 1000):
  x += 1
  count += 1

a = count

#het optellen van de datum vandaag plus aantal dagen tot verKdag
b = dataNu + timedelta(days=a)

print(f" Je volgende VerKdag is in {a} dagen!, dat is op {b}")