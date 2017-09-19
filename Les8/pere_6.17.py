def hexASCII():
    x = ord('a')-1
    while x < ord('z'):
        x+=1
        print('{}:{}'.format(chr(x),format(x,'02x')), end=' ')
hexASCII()