age = 63
hits = 9
shield = 5
if age > 62:
    print('You can get Social Securtiy Benefit')

if 'large bonuses' in 'report':
    print('Vacation time')

if hits > 10 and shield == 0:
    print("youre dead")


name = input('Voer uw naam in ')
age = int(input('Voer uw leeftijd in '))
if age >= 18:
    print('You can vote')
else:
    print("You can't vote")

def spelling():
    word = input('Voer woord in')
    for x in word:
        print(x)
spelling()

for x in range(11):
    print(x)
for x in range(1,10):
    print(x)
for x in range(0,9,2):
    print(x)
for x in range(1,10,2):
    print(x)
for x in range(20,61,10):
    print(x)