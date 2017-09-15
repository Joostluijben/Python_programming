def distrubution(file):
    content = open(file)
    lst = []
    list = content.readlines()
    for x in list:
        lst.append(x.split(' '))
    for x in lst:
        print(str(x.count('A'))+ ' students got an A')
        print(str(x.count('B')) + ' students got an B')
distrubution('grades.txt')