def BMI(weight,height):
    BMI = (weight*703)/height**2
    if BMI < 18.5:
        print('underweight')
    elif BMI <25:
        print('Normal')
    elif BMI >= 25:
        print('overweight')
BMI(240,75)

def acronym(user):
    for x in user.split():
        print(x[0].upper(),end='')
acronym('Random acces memory')