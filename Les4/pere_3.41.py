def hit(xC, yC, radC, xP, yP):
    if (xC+radC >= xP or xP <= xC+radC )and (yC+radC>=yP or yP <=yC+radC):
        print(True)
    else:
        print(False)
hit(0,0,5,5,5)