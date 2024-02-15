#-------------Détecter et éliminer les valeurs dupliquées-----------------

""" la liste ma_liste contient :
        3 x la valeur 'rouge'
        1 x la valeur 'vert'
        2 x la valeur 'orange'
        3 x la valeur 'bleu'
        1 x la valeur 'jaune' """

ma_liste = ["Rouge", "Vert", "Orange", "Bleu", "Bleu", "Rouge", "Jaune", "Orange", "Bleu", "Rouge"]

# création d'un dictionnaire
mon_dico = dict()

# ajout des valeurs de ma_liste dans mon_dico
for e in ma_liste :
    mon_dico[e] = 0

# creation d'un ensemble contenant les valeurs de mon_dico sans répétition d'occurence
mon_set = set(mon_dico.keys())

print(mon_set)

