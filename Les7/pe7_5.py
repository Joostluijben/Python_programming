def name():
    dic = {}
    userName = input('Voer een naam in ')
    if userName != '':
        if userName in dic:
            dic[userName] += 1
        else:
            dic[userName] = 1
    elif userName == '':
        print(dic)
    while userName != '':
        userName = input('Voer een naam in ')
        if userName != '':
            if userName in dic:
                dic[userName] += 1
            else:
                dic[userName] = 1
        else:
            print(dic)
name()