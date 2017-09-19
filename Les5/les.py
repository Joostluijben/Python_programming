s = 'Apple'
print(s[:-2])
print(s[-3:-1])

link = 'https://www.main.com/smith/index.html'
link[:4].replace('http', 'https')
print(link)
print(link.find('smith'))


pets = ['boa','cat', 'dog']
for x in pets:
    print(x,end='!!! ')
hour = 3
minute=14
second= 50
print('\n{}:{}:{}'.format(hour,minute,second))

lst = ['Alexander Turing', 'Ken Thompson', 'Vint Cerf']
for x  in lst:
    name = x.split()
    print('{:10} {}'.format(name[0], name[1]))


print('\n\n{:b}'.format(10))