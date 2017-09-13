cijfers = ('1','2','3','4','5','6','7','8','9','0')
def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        for x in newpassword:
            if x in cijfers:
                return print(True,'\nHet wachtwoord is veranderd')
        else:
            return print(False)
    else:
        return print(False)
new_password( 'hoi' , 'hoi' )
new_password('hallo_daar', 'hallo_daaro')
new_password('hallo_daar', 'hallo_daaro2')
new_password(input('voer uw oude wachtwoord in : '), input('voer uw nieuwe wachtwoord in dat niet hetzelfde is als uw oude, langer is dan 6 karakters en 1 cijfer bevat: '))