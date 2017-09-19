def week():
    dic ={'Mon':'Monday', 'Tue':'Tuesday'}
    user = input('Enter day abbrevation: ')
    print(dic[user])
    while user != '':
        user = input('Enter day abbrevation: ')
        print(dic[user])
week()