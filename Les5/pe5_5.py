def calculate():
    sentence = input('Voer een willekeurige zin in ')
    lst = []
    words = []
    number = []
    lst.append(sentence)
    for x in lst:
        words.append((x.split(' ')))
    for x in words:
        for s in x:
            number.append(len(s))
    average =  float(sum(number)/len(number))
    print('De gemiddelde lengte van de woorden in de zin is ' +str(average))
calculate()