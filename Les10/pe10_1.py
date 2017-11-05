import xmltodict

with open('artikelen.xml') as artikelenReadXml:
    artikeldict = xmltodict.parse(artikelenReadXml.read())
for artikelNaam in artikeldict['artikelen']['artikel']:
    print(artikelNaam['naam'])
