stations = ['Schagen', 'Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Solterdijk','Amsterdam Centraal','Amsterdam Amstel',
            'Utrecht Centraal',"'s-Hertogenbosch",'Eindhoven','Weert','Roermond', 'Sittard', 'Maastricht']


def inlezen_beginstation(stations):
    begin = input('Wat is je beginstation? : ')
    while True:
        if begin in stations:
            return begin
        else:
            print('Dat is geen geldig station')
            begin = input('Wat is je beginstation? :')

def inlezen_eindstation(stations,beginstation):
    eind = input('Voer een eindstation in? : ')
    while True:
        if eind in stations:
            if stations.index(eind) > stations.index(beginstation):
                return eind
            else:
                print('Dat station komt niet voor het beginstation ')
                inlezen_beginstation(stations)
        else:
            print('Dat is geen geldig station')
            eind = input('Wat is je eindstation? : ')

def omroepen_reis(stations, beginstation, eindstation):
    afstand = stations.index(eindstation)-stations.index(beginstation)
    ritprijs = int(afstand) * 5
    print('Het beginstation '+str(beginstation)+' is het '+str(stations.index(beginstation)+1) + 'e in het traject')
    print('Het eindstation '+ str(eindstation)+' is het ' +str(stations.index(eindstation)+1)+'e in het traject')
    print('De afstand bedraagt ' + str(afstand)+' station(s)')
    print('De prijs van het kaartje is '+ str(ritprijs)+' euro')
    print('Jij stapt in de trein in: '+str(beginstation))
    for x in range(1,stations.index(eindstation)-stations.index(beginstation)):
        print('- ' + stations[x], sep='-\n')
    print('Jij stapt uit in: '+ eindstation)
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
