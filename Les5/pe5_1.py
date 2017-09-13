def convert (temperatuur):
    return temperatuur*1.8+32
#convert(int(input('Voer het aantal graden Celsius in: ')))


def tabel():
    print('F\t\tC''')
    for x in range(-30,41,10):
        Fh = convert(x)
        print(x,Fh, sep='\t\t')
tabel()
