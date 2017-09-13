students = []
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
count = int(input('Hoeveel studenten wilt u invoeren? '))
for x in range(count):
    students.append(input('Voer een naam in '))
for i in students:
    if i[0] in letters:
        print(i)