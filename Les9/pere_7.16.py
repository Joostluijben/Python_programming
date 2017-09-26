def index(file, lst):
    try:
        open(file)
    except FileNotFoundError:
        print(str(file)+' bestaat niet')


index('rven.txt',[['raven', 'mortal', 'dying', 'ghost']])
