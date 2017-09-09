age = int(input('Geef je leeftijd:'))
paspoort = eval(input('Nederlands paspoort:'))
if (age >= 18) and (paspoort == True):
    print('Gefeliciteerd, je mag stemmen!')
elif (paspoort != True) or age <= 18:
    print('Helaas u mag niet stemmen')
