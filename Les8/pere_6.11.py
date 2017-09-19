def easyCrypto():
    string = input('Voer iets in ')
    for x in string:
        if ord(x)%2!=0:
            print(chr(ord(x)+1),end='')
        elif ord(x)%2==0:
            print(chr(ord(x)-1),end='')
easyCrypto()
