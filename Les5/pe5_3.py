def counting(file):
    content = open(file, 'r')
    reader = content.read()
    print('Deze file heeft '+str(reader.count('\n')+1)+ ' regels')
    content.close()
    content = open(file, 'r')
    lst = []
    numbers = []
    reader = content.readlines()
    for x in reader:
        lst.append(x.strip().split(','))
    for x in lst:
        numbers.append(x[0])
    maximumNumber= max(numbers)
    lineNumber = numbers.index(max(numbers))+1
    print('Het grootste kaartnummer is: '+ str(maximumNumber)+' en dat staat op regel ' + str(lineNumber))
counting('kaartnummers.txt')