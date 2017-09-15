s = '10 20 30 40 50 60'
lst = s.split()
print(lst)
i  = '10,20,30,40,50,60'
lsti = i.split(',')
print(lsti)
l = '10&20&30&40&50&60'
lstl = l.split('&')
print(lstl)

def plist():
    p = '10 - 20 - 30 - 40 - 50 - 60'
    p.strip()
    p.split('-')
    print(p)
plist