invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
numbers = invoer.split('-')
lst = []
numbers.sort()
maximum = max(numbers)
minimum = min(numbers)
count = len(numbers)
for x in numbers:
    lst.append(eval(x))
optel = sum(lst)
average = optel/count
print('Gesorteerde list van ints: ' + str(numbers))
print('Grootste getal: ' + str(maximum) + ' en het Kleinste getal ' + str(minimum))
print('Aantal getallen: ' + str(count) + ' en Som van de getallen: ' + str(optel))
print('Gemiddelde: ' + str(average))