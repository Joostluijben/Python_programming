def monopolyworp():
    import random
    count = 0
    x = random.randrange(1, 7)
    y = random.randrange(1, 7)
    p = x + y
    while count < 3:
        if x == y:
            x = random.randrange(1, 7)
            y = random.randrange(1, 7)
            p = x + y
            count += 1
            if count < 3:
                print('{} + {} = {} (dubbel)'.format(x, y, p))
            elif count == 3:
                print('{} + {} = {} (direct naar gevagenis)'.format(x, y, p))
        else:
            print('{} + {} = {}'.format(x, y, p))
            break


monopolyworp()
