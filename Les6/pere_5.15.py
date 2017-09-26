user = input('Voer een string in ')
for x in user:
    if x in 'aeiouAEIOU':
        print(user.index(x))