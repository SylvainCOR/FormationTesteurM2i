import random

def generer_id(nb_lettres, nb_chiffres) -> str :
    
    liste_lettre = "R", "Z", "S", "X", "W", "T"
    lettres = ""
    while len(lettres) < nb_lettres :
        lettres += random.choice(liste_lettre)
    
    nombre_str = str(random.randint(0, 9999 + 1))
    
    return f"{lettres}-{nombre_str.zfill(nb_chiffres)}"


NB_LETTRES = 3
NB_CHIFFRES = 4

print(generer_id(NB_LETTRES, NB_CHIFFRES))