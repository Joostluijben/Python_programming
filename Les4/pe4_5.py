def kwadraten_som(grondgetallen):
    sum = 0
    for x in grondgetallen:
        if x > 0:
            sum = sum+x
    return print(sum)
kwadraten_som([-1,2,3,5])