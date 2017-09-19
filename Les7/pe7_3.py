cursus = {
    'Joost':8,
    'Piet':6,
    'Klaas':10,
    'Ilse':9,
    'Hans':7.8,
    'Franka':8.8,
    'Grietje':4.4,
    'Jan':1.2
}
for name, note in cursus.items():
    if note > 8.0:
        print('{:6}{:6}'.format(name,note))
