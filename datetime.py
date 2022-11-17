from datetime import datetime, date, timedelta

Verjaardag = input("Geef je geboortedatum in dag/maand/jaar: ")
dataVerjaardag = datetime.strptime(Verjaardag, '%d/%m/%Y').date()
dataNu = datetime.date(datetime.now())

data_verschil = (dataNu - dataVerjaardag).days

a = data_verschil

x = (a % 1000)

count = 0

while (x < 1000):
  x += 1
  count += 1

a = count
b = dataNu + timedelta(days=a)

print(f" Je volgende VerKdag is in {a} dagen!, dat is op {b}")