#-------------------Afficher résultats + - / * de 2 nombres-----------------------

def afficher_resultats(s, d, q, p) :
    print("\n\tSomme = ", s, "\n\tDifférence = ", d,\
            "\n\tQuotient = ", q, "\n\tProduit = ", p, "\n")  

def muli_calcul(nb_1, nb_2) :
    tuple = nb_1 + nb_2, nb_2 - nb_1, nb_2 / nb_1, nb_1 * nb_2
    # arrondi tous les éléments de la liste à 2 décimales
    tuple = (round(item, 2) for item in tuple)
    return tuple

def demander_nombres() :
    return float(input("Entrez le premier nombre : ")),\
            float(input("Entrez le second nombre : "))


# demande les nombres à l'utilisateur 
nb_1, nb_2 = demander_nombres()

# crée une liste avec le résultat des calculs souhaités
tuple = muli_calcul(nb_1, nb_2)

# affiche les résultats en séparant le tuple
afficher_resultats(*tuple)


