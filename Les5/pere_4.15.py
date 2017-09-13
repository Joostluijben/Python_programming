s = '10 20 30 40 50 60'
lst = s.split()
print(lst)
i  = '10, 20, 30, 40, 50, 60'
lsti = i.split()
for x in lsti:
    x[:-2]
print(lsti)