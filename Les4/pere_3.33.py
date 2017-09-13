def prob(n):
    n = int(input('Voer een getal in dat hoger is dan 0 '))
    if n < 0:
        print('Dat getal is niet hoger dan 0')
    elif n > 0:
        print(2**n)
prob(1)