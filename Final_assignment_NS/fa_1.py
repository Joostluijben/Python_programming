def standaardprijs(afstandKM):
    if afstandKM > 50:
        print('De normale prijs is '+ str((afstandKM*0.60)+15))
    elif afstandKM < 50 and afstandKM > 0:
        print('De normale prijs is '+ str(afstandKM*0.80))
    else:
        print('U kunt geen negatieve afstand invoeren, de prijs is daardoor '+str(afstandKM*0))

def ritprijs(leeftijd,weekendrit,afstandKM):
    standaardprijs(afstandKM)
    if ((leeftijd < 12 and leeftijd > 0) or leeftijd >= 65) and afstandKM > 0:
        if weekendrit == 0:
            print('De prijs inclusief korting is '+str(afstandKM-(afstandKM/100*30)))
        elif weekendrit == 1:
            print('De prijs inclusief koring is ' + str(afstandKM-(afstandKM/100*35)))
    elif leeftijd > 12 and leeftijd <= 65 and afstandKM > 0:
        if weekendrit == 1 and afstandKM > 0:
            print('De prijs inclusief korting is ' + str(afstandKM - (afstandKM / 100 * 40)))
    elif leeftijd < 0:
        print('Dat is geen geldige leeftijd')
ritprijs((int(input('Voer uw leeftijd in: '))), bool(input('Reist u in het weekend? ')), int(input('Hoeveel kilometer reist u? '))) 