def avg():
    lst = []
    count = int(input('Hoeveel studenten wilt u invoeren '))
    for x in range(count):
        for s in range(x):
            lst.append(eval(input('Voer lijst me de cijfers van de leerlingen in ')))
    for i in range(count):
        average = sum(lst[i])
        print(average)
avg()
