def code(invoersstring):
    for x in invoersstring:
        encyrpt = ord(x)+3
        print(chr(encyrpt), end='')
code('RutteAlkmaarDen Helder')