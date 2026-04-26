# Napis funkci zamen(retezec, pozice, znak)

# Tato funkce vrátí řetězec, který má na dané pozici daný znak; jinak je stejný jako původní retezec. Např:
#
# zamen('palec', 0, 'v') == 'valec'
# zamen('valec', 2, 'j') == 'vajec'
def zamen(retezec, pozice, znak):    #toto je verze pro ajtaky:-)
   zmeneny_retezec = retezec[:pozice-1]+znak+retezec[pozice:]
   print(zmeneny_retezec)
zamen('kamna',4,'p')

def zamen():    #toto je verze interaktivni
    retezec = input(str('Zadej slovo ke zmene: '))
    pozice = int(input('Zadej pozici zmeny: '))
    znak = input(str('Zadej zmeneny znak: '))

    zmeneny_retezec = retezec[:pozice-1]+znak+retezec[pozice:]
    print(zmeneny_retezec)

zamen()


