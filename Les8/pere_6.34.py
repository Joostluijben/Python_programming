def game(user):
    import random
    count = 0
    for x in range(user):
        t = random.randrange(0, 10)
        y = random.randrange(0, 10)
        p = t + y
        print(t,y)
        answer = int(input('Voer een getal in: '))
        if answer== p:
            print('Correct')
            count +=1
        else:
            print('Incorrect')
    print('You got ' +str(count) +' out of ' + str(user))
game(3)