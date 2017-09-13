def f(x):
    res = x**2+10
    return print(res)
f(10)

def hello():
    name = input('Voer naam in ')
    print('Welcome, ' + str(name) + ', to the world of Python: ')
#hello()

def swapFS(lst):
    if len(lst)>=2:
        lst[0], lst[1] = lst[1], lst[0]
        print(lst)
        lst.pop()
        print(lst)
    else:
        print(lst)
swapFS(['one','two'])