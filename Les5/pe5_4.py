import datetime

name = input('Voer een naam in ')
hour = int(input('Voer een uur in '))
minute = int(input('Voer een minuut in '))
second = int(input('Voer een seconde in '))
formatted = datetime.datetime(2016,5,10,hour, minute, second)
s = formatted.strftime("%a %d %b %Y, %X")
'{}, {}'.format(s,name)
outfile = open('marathon.txt', 'a')
outfile.write('{}, {}'.format(s,name)+str('\n'))
outfile.close()