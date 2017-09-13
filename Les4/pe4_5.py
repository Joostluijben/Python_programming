def kwadraten_som(grondgetallen):
    sum = 0
    for x in grondgetallen:
        if x > 0:
            sum = sum+(x**2)
    return print(sum)
kwadraten_som([4,5,-81,3])
