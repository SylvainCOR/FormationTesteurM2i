#-------------Recherche d'une valeur dans un tableau ordonné-----------------

def chercher_valeur(valeur, tab):
    # recharche de valeur dans tab
    for i in range(0, len(tab)) :
        if valeur == tab[i] :
            return i
    return None

liste = [5, 2, 0, 8, 3, 9, 1, 6, 4, 7]
print(chercher_valeur(6, liste))
print(chercher_valeur(10, liste))
