s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = ['a', 'e', 'i', 'o', 'u']
for x in s:
    if x in klinkers:
        print(x)