lst = []
count = 0
count_user = eval(input('Voer aantal keer in '))
if count_user > 0:
    for x in range(count_user):
        lst.append(input('Voer een waarde in voor de list '))
    #while count < count_user:
    #    lst.append(input('Voer waarde in voor de list '))
    #    count = count+ 1
elif count_user <= 0:
    print('Voer een nummer in dat hoger is dan 0 ')
if 'secret' not in lst:
    for x in lst:
        print(x)
elif 'secret' in lst:
   for x in range(lst.count('secret')):
       lst.remove('secret')
   for x in lst:
       print(x)
