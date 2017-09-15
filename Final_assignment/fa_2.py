def toon_aantal_kluizen_vrij():
    lst = []
    content = open('kluizen.txt')
    reader = content.readlines()
    for x in reader:
        if x != '\n':
            lst.append(x.strip())
    vrij = 12 - len(lst)
    print('Er zijn '+str(vrij) + ' kluisjes vrij\n')



def nieuwe_kluis():
    lst = []
    kluisnummers = []
    content = open('kluizen.txt','r')
    reader = content.readlines()
    content.close()
    for x in reader:
        lst.append(x.strip().split(';'))
    for x in lst:
        kluisnummers.append(int((x[0])))
    nummer = int(input('Voer een kluisnummer in '))
    if len(kluisnummers) == 12:
        print('Er zijn geen kluisjes meer vrij')
    elif nummer in kluisnummers:
        print('Dat kluisje is bezet')
    elif nummer not in kluisnummers and nummer <12:
        code = input('Voer een kluiscode in ')
        content = open('kluizen.txt','a')
        content.write(str('\n')+'{};{}'.format(nummer,code))
        print('U heeft kluisje '+str(nummer)+' gekregen')
    elif nummer > 12:
        print('Er zijn maar 12 kluisjes')



def kluis_openen():
    lst = []
    nummer = input('Voer een kluisnummer in ')
    code = input('Voer uw code in ')
    content = open('kluizen.txt')
    reader = content.readlines()
    content.close()
    for x in reader:
        lst.append(x.strip().split(';'))
    for x in lst:
        if nummer == x[0] and code == x[1] and 12 >= int(nummer):
            stop = print('U kunt uw kluisje openen\n')
            return stop
        elif int(nummer) > 12:
            print('Er zijn maar 12 kluisjes')
            break
    else:
        print('Dat is geen juiste wachtwoord en kluisnummer combinatie\n')




def kluisteruggeven():
    lst=[]
    nummer = input('Voer een kluisnummer in ')
    code = input('Voer uw code in ')
    content = open('kluizen.txt', 'r')
    reader = content.readlines()
    for x in reader:
        lst.append(x.strip().split(';'))
    for x in lst:
        if nummer in x[0] and int(nummer) <13:
            if nummer==x[0] and code==x[1]:
                lst.remove(x)
                print('Uw kluis is teruggegeven\n')
                content.close()
        elif int(nummer) > 12:
            print('Er zijn maar 12 kluisjes')
            break
    content = open('kluizen.txt', 'w')
    for x in lst:
        formatted = ('{};{}'.format(x[0],x[1]))+str('\n')
        content.write(formatted)





loop = 1
while True:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug\n5: Sluit af')
    user = input('Maak uw keuze ')
    if user == '1':
        toon_aantal_kluizen_vrij()
    elif user == '2':
        nieuwe_kluis()
    elif user == '3':
        kluis_openen()
    elif user == '4':
        kluisteruggeven()
    elif user == '5':
        break
