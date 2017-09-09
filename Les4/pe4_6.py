lijst = ['a', 'b', 'c']
print(lijst)
def wijzig(letterlijst):
    lijst.pop()
    lijst.pop()
    lijst.pop()
    lijst.append('d')
    lijst.append('e')
    lijst.append('f')
wijzig(lijst)
print(lijst)