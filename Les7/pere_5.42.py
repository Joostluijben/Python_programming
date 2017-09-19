def primeFac():
    n = int(input('Voer een positef getal in '))
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n = n /d
        d = d + 1

    print(factors)
primeFac()
