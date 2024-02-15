#-------------Algorithme de tri diviser pour règner-----------------

def div_tri(tab) :
    if len(tab) > 1 :
        milieu = len(tab) // 2
        tab_gauche = tab[:milieu]
        tab_droit = tab[milieu:]

        # appel recursif pour la division des tableaux
        div_tri(tab_gauche)
        div_tri(tab_droit)
    
        # procédure de fusion
        i = 0 # indice utilisé avec tab_gauche
        j = 0 # indice utilisé avec tab_droit
        k = 0 # indice utilisé avec tab résultat de la fusion
        
        # extraction des valeurs des 2 tableaux
        while i < len(tab_gauche) and j < len(tab_droit) :
            if tab_gauche[i] < tab_droit[j] :
                tab[k] = tab_gauche[i]
                i += 1
            else :
                tab[k] = tab_droit[j]
                j += 1
            k += 1
        
        # traitement des données restantes dans tab_gauche
        while i < len(tab_gauche) :
            tab[k] = tab_gauche[i]
            i += 1
            k += 1

        # traitement des données restantes dans tab_droit
        while j < len(tab_droit) :
            tab[k] = tab_droit[j]
            j += 1
            k += 1

liste = [5, 2, 0, 8, 3, 9, 1, 6, 4, 7]
print("Début de la procédure de tri sur la liste :", liste)
div_tri(liste)
print("Résultat du tri :", liste)

