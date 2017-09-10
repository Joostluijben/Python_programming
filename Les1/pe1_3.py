#Schrijf Python statements die het volgende doen:
#1. Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b.
#2. Ken aan variabele c als waarde het gemiddelde van a en b toe.
#3. Ken aan variabele inventaris de een lijst van strings toe: ‘papier’, ‘nietjes’, en ‘pennen’.
#4. Ken aan variabelen voornaam, tussenvoegsel en achternaam je eigen naamgegevens toe.
#5. Ken aan variabele mijnnaam de variabelen van opdracht 4 (met spaties er tussen) toe.
#Schrijf booleaanse expressies die van de variabelen van Practice Exercise 1_3 evalueren of:
#1. 6.75 groter is dan a en kleiner b.
#2. de lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam.
#3. de lijst inventaris leeg is, of juist meer dan 10 items bevat.


a=6
b=7
c=(a+b)/2
print(c)

inventaris = ['papier', 'nietjes ', 'pennen']
voornaam = 'Joost'
tussenvoegsel = ''
achternaam = 'Luijben'
mijnNaam= voornaam + ' ' + tussenvoegsel + '' + achternaam
print(mijnNaam)
print(6.75>a and 6.75<b)
print((len('inventaris') * 5) > len(mijnNaam))
(print(len(inventaris) == 0) or (len(inventaris)>10))
