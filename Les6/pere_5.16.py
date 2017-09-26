def indexes():
    user = input('Voer een string in ')
    vowel = input('Voer een letter in ')
    for x in user:
        if vowel in x:
            print(user.index(x))


indexes()
