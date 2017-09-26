value = 4356
try:
    user = int(input('Hoeveel personenen gaan er mee? '))
    if user < 0:
        print('Negatieve getallen zijn niet toegestaan!')
    else:
        print(value/user)
except ZeroDivisionError:
    print('Delen door 0 kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')