def censor(file):
    content = open(file,'r')
    writer = open('censored.txt','w')
    reader = content.readlines()
    lst = []
    for x in reader:
        lst.append(x.split(' '))
    for x in lst:
        for s in x:
            if len(s) == 4:
                writer.write(s.replace(s, 'xxxx '))
            else:
                writer.write(s+str(' '))
censor('file.txt')