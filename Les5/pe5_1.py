def convert (temperatuur):
    print(temperatuur*1.8+32)
#convert(int(input('Voer het aantal graden Celsius in: ')))


def tabel():
    for x in range(-30,41,10):
        print(x), convert(x)
tabel()
