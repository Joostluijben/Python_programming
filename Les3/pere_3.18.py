import math

a, b, c = 3, 4, 5
if a < b:
    print('OK')
elif a > b:
    print('NOT OK')

if c < b:
    print('OK')
elif c > b:
    print('NOT OK')

if (a+b) == c:
    print('OK')
elif (a+b) != c:
    print('NOT OK')

if math.sqrt(a + b) == math.sqrt(c):
    print('OK')
elif math.sqrt(a + b) != math.sqrt(c):
    print('NOT OK')
