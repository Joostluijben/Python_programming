lijst = ['a', 'b', 'c']

def wijzig(letterlijst):
    lijst.pop()
    lijst.pop()
    lijst.pop()
    lijst.append('d')
    lijst.append('e')
    lijst.append('f')
print(lijst)
wijzig(lijst)
print(lijst)