import random

namen = ['Claire', 'Christy', 'Joost']
namen.append('Noah')
random_number = int(random.choice([0, 1, 2, 3]))
namen.remove(random_number)
print(namen)
