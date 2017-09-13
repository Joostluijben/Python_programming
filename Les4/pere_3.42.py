def ion2e():
    word = input('Voer een woord in ')
    if 'ion' in word:
        cut = word[:-3]
        add = cut+'e'
        print(add)
    else:
        print(word)
ion2e()