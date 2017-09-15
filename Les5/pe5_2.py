infile = open('kaartnummers.txt')
lst = []
content = infile.readlines()
for x in content:
    lst.append(x.split(','))

infile.close()
for x in lst:
    print(x[1].strip() + 'heeft kaartnummer: ' + x[0])
