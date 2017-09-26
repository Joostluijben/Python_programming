count = 0
counter = 0
while True:
    if count < 2:
        try:
            user = int(input('Please enter a number: '))
            counter += user
            if user == 0:
                print(counter)
                break
        except ValueError:
            print('Error. Please re-enter the value.')
            count += 1
    else:
        print('Two errors in a row. Quitting ...')
        break
