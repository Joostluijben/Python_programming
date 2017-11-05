import xmltodict
import datetime
import authorise
import time

authorise.writeXML()

with open('departures.xml') as readDepartureXml:
    stationsdict = xmltodict.parse(readDepartureXml.read())


def trainDepature(destination):
    for trains in stationsdict['ActueleVertrekTijden']['VertrekkendeTrein']:
        try:
            if (destination in trains['EindBestemming']) or (destination in trains['RouteTekst']):
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

        except KeyError:
            continue
