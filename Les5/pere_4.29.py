
def stats(file):
    countLine = 0
    content = open(file)
    for x in content:
        if '\n' in x:
            countLine += 1
    print('line count: '+ str(countLine))
    content.close()
    content = open(file)
    readWord = content.readlines()
    print('word count: '+ str(len(readWord)))
    content.close()
    content = open(file)
    reader = content.read()
    print('character count: '+ str(len(reader)))
    content.close()
stats('example.txt')