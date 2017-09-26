import csv
lst = []
with open('gamers.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=';')
    for x in reader:
        if int(x[2])
