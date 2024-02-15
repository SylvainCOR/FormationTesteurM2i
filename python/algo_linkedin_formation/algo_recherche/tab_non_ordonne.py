#-------------Algo de recherche dichotomique (binaire)-----------------

def rechercher_bin(valeur, tab):
    longueur = len(tab) - 1
    # les 2 indices de recherche
    inf = 0
    sup = longueur

    while inf <= sup :
        # centre du tableau
        milieu = (inf + sup) // 2
        
        if tab[milieu] == valeur :
            return milieu
        elif valeur > tab[milieu] :
            inf = milieu + 1
        else :
            sup = milieu - 1
        
    if inf > sup :
        return None
            
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rechercher_bin(5, liste))
print(rechercher_bin(10, liste))
