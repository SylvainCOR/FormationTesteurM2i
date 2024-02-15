#-------------Algorithme de tri rapide (quicksort)-----------------

def tri_rapide(tab, indice_1, indice_2) :    
    if indice_1 < indice_2 :
        print(tab)
        # chercher le point de séparation
        milieu = coupe(tab, indice_1, indice_2)

        # appels récursifs pour trier les 2 sous tableaux
        tri_rapide(tab, indice_1, milieu - 1)
        tri_rapide(tab, milieu + 1, indice_2)
        
def coupe(tab, indice_1, indice_2) :
    pivot = tab[indice_1]
    
    # positionnement des 2 indices inf eu sup
    inf = indice_1 + 1
    sup = indice_2
    
    end = False
    while not end :
        # avancer l'indice inf d'une position
        while inf <= sup and tab[inf] <= pivot :
            inf += 1
        
        # reculer l'indice sup d'une position
        while sup >= inf and tab[sup] >= pivot :
            sup -= 1
        
        if sup < inf :
            end = True
        else :
            temp = tab[inf]
            tab[inf] = tab[sup]
            tab[sup] = temp
    
    # positionnement du point pivot
    temp = tab[indice_1]
    tab[indice_1] = tab[sup]
    tab[sup] = temp

    # retouner la valeur de l'indice sup
    return sup

liste = [5, 2, 0, 8, 3, 9, 1, 6, 4, 7]
print("Début de la procédure de tri sur la liste :", liste)
tri_rapide(liste, 0, len(liste) - 1)
print("Résultat du tri :", liste)

