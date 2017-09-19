            #Geordend   Muteerbaar Iterable Dubbele waarden toegestaan
#Tuple      Nee         Nee         Ja      Ja
#Dictonairy Nee         Nee         Ja      Nee
#Set        Nee         Nee         Ja      Nee
#List       Nee         Ja          Ja      Ja




tuple = ('hoi','doei')
print(tuple)
print(type(tuple))
#tuple[1]='doei'
for x in tuple:
    print(x)

dic = {'hallo':'hoi',
       'tot ziens':'doei',
       '':''}
print(dic)
print(type(dic))
dic['hallo'] = 'wat'
print(dic)
for x in dic:
    print(x)

sett = {('hoi'),( 'doei')}
print(sett)
print(type(sett))
#sett['hoi'] ='wat'
print(sett)
for x in sett:
    print(x)
sett = {('hoi'),( 'doei'),( 'doei')}
print(sett)
lst = ['hoi', 'doei']
print(lst)
print(type(lst))
lst[0]= 'hallo'
print(lst)
for x in lst:
    print(x)
lst = ['hoi','doei','doei']
print(lst)