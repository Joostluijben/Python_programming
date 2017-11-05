import requests

auth_details = ('joost.luijben@yahoo.com', 'C1t1p9MIBDuqwi26CRnGfNnN_BZ-OkRjmSeiyf57nW9WmSUd1MWJPQ')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

response = requests.get(api_url, auth=auth_details)

with open('departures.xml', 'w') as writeDepartureXml:
    writeDepartureXml.write(response.text)
