age = int(input('Geef je leeftijd:'))
paspoort = input('Nederlands paspoort:')

if (age >= 18) and (paspoort == 'ja'):
    print('Gefeliciteerd, je mag stemmen!')
elif (paspoort != 'ja') or (age <= 18):
    print('Helaas u mag niet stemmen')
