lstOld = eval(input('Geef een lijst met minimaal 10 strings op'))
lst = []
if len(lstOld) >= 10:
    for x in lstOld:
        lst.append(x)
    print(lst)
else:
    print('De lijst is niet 10 strings')
# ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]