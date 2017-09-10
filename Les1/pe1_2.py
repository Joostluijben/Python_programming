#Schrijf en evalueer Python expressies die de volgende vragen beantwoorden:
#a. Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
#b. Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?
#c. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
#d. Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian',
#'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst?



#a
print(len('Supercalifragilisticexpialidocious'))
#b
print('ice' in ('Supercalifragilisticexpialidocious '))
#c
print(len('Antidisestablishmentarianism') > len('Honorificabilitudinitatibus'))
#d
componist = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Bernstein']
componist.sort()
print(componist)
print(componist[0])
print(componist[-1])