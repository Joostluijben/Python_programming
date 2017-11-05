import xmltodict
import datetime
import authorise
import time

authorise.writeXML()

with open('departures.xml') as readDepartureXml:
    stationsdict = xmltodict.parse(readDepartureXml.read())
def trainDepature():
    for trains in stationsdict['ActueleVertrekTijden']['VertrekkendeTrein']:
        try:
            if (trains['EindBestemming'] == 'Utrecht Centraal') or ('Utrecht C' in trains['RouteTekst']):
                departure = trains['VertrekTijd'][11:16]
                timeNow = datetime.datetime.strptime(datetime.datetime.today().strftime('%H:%M'), '%H:%M')
                departureTime = datetime.datetime.strptime(departure, '%H:%M')
                timeDifference =  datetime.datetime.strptime(departure, '%H:%M') - timeNow
                hoursDifference = int(str(timeDifference)[0:1])
                hoursDifferenceToMinutes = int(hoursDifference * 60)
                minutesDifference = int(str(timeDifference)[2:4])
                totalDifference = hoursDifference + minutesDifference

                trainKind = trains['TreinSoort']
                print('The next train ({}) leaves in {} minutes'.format(trainKind, totalDifference))

                if totalDifference >=15:
                    print('You can catch this train!\n')
                elif totalDifference < 15 and totalDifference > 10:
                    print('You might be able to catch this train if you leave now!\n')
                else:
                    print("You can't catch this train anymore, sorry :(\n")

        except KeyError:
            continue
    print('---------------------------------------------------------')

while True:
    trainDepature()
    time.sleep(60)
