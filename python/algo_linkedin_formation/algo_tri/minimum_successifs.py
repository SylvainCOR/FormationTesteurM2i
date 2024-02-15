#-------------Algorithme de tri des minimums successifs-----------------

def tri_min(tab):
    print("Début de la procédure de tri sur la liste :", tab)
    for i in range(len(tab)-1) :
        # recherche du min entre l'indice i et la fin du tableau
        for j in range(i + 1, len(tab)) :
            if tab[i] > tab[j] :
                temp = tab[j]
                tab[j] = tab[i]
                tab[i] = temp
        print(f"L'état de tri à l'étape {i + 1} est : {tab}")

liste = [5, 2, 0, 8, 3, 9, 1, 6, 4, 7] 

tri_min(liste)
print("Résultat du tri :", liste)
