#-------------Algo de recherche de la valeur minimale et de la valeur maximale dans une liste-----------------

def min_max(liste) :
    # initialisation min et max à la 1ere valeur de la liste
    max = liste[0]
    min = liste[0]
    
    for i in range(len(liste)) :
        if max < liste[i] :
            max = liste[i]
        if min > liste[i] :
            min = liste[i]
    
    return(min, max)

ma_liste = [5, -2, 0, 18, 13, 1000, -14, 6, -1000, 67]
min, max =  min_max(ma_liste)
print(f"Valeurs mini : {min} et maxi : {max}")