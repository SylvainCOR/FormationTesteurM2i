#-------------Algorithme de tri à bulle-----------------

def tri_bulle(tab):
    print("Début de la procédure de tri sur la liste :", tab)    
    for i in range(len(tab) - 1, 0, -1) :
        # remonter le max à la dernière position de la liste
        for j in range(i):    
            if tab[j] > tab[j + 1] :
                temp = tab[j]
                tab[j] = tab[j + 1]
                tab[j + 1] = temp
        print(f"L'état de tri à l'étape {len(tab) - i} est : {tab}")

liste = [5, 2, 0, 8, 3, 9, 1, 6, 4, 7] 

tri_bulle(liste)
print("Résultat du tri :", liste)
