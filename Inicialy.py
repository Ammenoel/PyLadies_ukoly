# Napis program, který:
# 1. se zeptá na jméno,
# 2. pak na příjmení
# 3. pak vypíše iniciály – první písmena zadaneho jmena a prijmeni

#Napr.
# Jmeno: Petr, Prijmeni: Novak => PN
# Jmeno: petr, Prijmeni: novak => PN

def inicialy():
    jmeno = input(str('Zadej sve jmeno: '))
    prijmeni = input(str('Zadej sve prijmeni: '))
    iniciala_jmeno = jmeno.upper()
    iniciala_prijmeni = prijmeni.upper()
    print('Tve inicialy jsou '+iniciala_jmeno[0]+iniciala_prijmeni[0]+'.')

inicialy()