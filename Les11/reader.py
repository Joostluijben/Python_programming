import xmltodict
with open('departures.xml') as readDepartureXml:
    stationsdict = xmltodict.parse(readDepartureXml.read())

for trainKind in stationsdict['ActueleVertrekTijden']['VertrekkendeTrein']['TreinSoort']:
    print(trainKind)
