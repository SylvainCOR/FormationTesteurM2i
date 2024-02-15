#-------------Nb d'occurences de la séquence ADN dans la chaîne ADN--------------

def verif_adn(adn) :
    # true / false si la chaine est valide ou non
    for lettre in adn :
        if lettre not in "atcg" :
            return False      
    return True

def saisie_adn(saisie) :
    # renvoie une chaine adn après verif
    while not verif_adn(saisie) :
        print("La saisie ne correspont pas à un ADN, veuillez recommencer.")
        demander_adn() # redemande la saisie car non valide
    return saisie # renvoie saisie valide
    
def proportion(chaine, sequence) :
    # renvoie % occurences de la séquence dans la chaine
    nb_occur = 0
    if sequence in chaine :
        nb_occur = chaine.count(sequence) # recherche du nombre d'occurences
                
    print(f"\nIl y a {nb_occur} occurences de la séquence dans la chaîne ADN") 
    
    pourcent = (nb_occur * len(sequence)) * 100 / len(chaine) # calcul du % d'occurences
    return round(pourcent, 2)
    
def demander_adn() :
    # demande à l'utilisateur de saisir chaine adn et séquence adn
    return input("\nEntrez une chaîne ADN : "), input("Entrez une séquence ADN : ")

