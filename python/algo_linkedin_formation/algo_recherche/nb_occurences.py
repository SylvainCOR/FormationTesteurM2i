#-------------Calcul du nombre d'occurences de chaque valeurs-----------------

""" la liste ma_liste contient :
        3 x la valeur 'rouge'
        1 x la valeur 'vert'
        2 x la valeur 'orange'
        3 x la valeur 'bleu'
        1 x la valeur 'jaune' """

ma_liste = ["Rouge", "Vert", "Orange", "Bleu", "Bleu", "Rouge", "Jaune", "Orange", "Bleu", "Rouge"]

# création d'un dictionnaire
mon_dico = dict()

# calcul du nombre d'occurence de chaque valeurs de ma_liste en utilisant les clés de la table de hachage mon_dico
for e in ma_liste :
    if e in mon_dico.keys() :
        mon_dico[e] += 1
    else :
        mon_dico[e] = 1

print(mon_dico)

