def hello2():
    user = input('What is your name? ')
    print('Hello ' + user)
    while user != '':
        user = input('What is your name? ')
        print('Hello ' + user)


# hello2()

phonebook = {('Anna', 'Karenina'): '(123)456-78-90', ('Yu', 'Tsun'): '(901)234-56-78',
             ('Hans', 'Castorp'): '(321)908-76-54'}


def lookup(phone):
    while True:
        firstName = input('What is the first name ')
        lastName = input('What is the last name')
        for x, y in phonebook.items():
            if x[0] == firstName and x[1] == lastName:
                print(y)


lookup(phonebook)
