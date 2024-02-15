import random

""" def combi_secrete (nb_lettres : str, liste_lettre : list) -> list :
    
    return random.sample(liste_lettre, k=nb_lettres)


def placement_lettres(combi : list, essai : list) -> str :
    
    for i in range(len(combi)) : 
        lettre_placee = ""
        if combi[i] == essai[i] :
            lettre_placee += essai[i]
    print(f"dont bien placées : {lettre_placee}\n" if lettre_placee != "" else "mais aucune bien placée...\n")


def comparaison (combi : list, essai : list, nb_essai : int) -> str :
    
    if combi == essai :
        print(f"\nBravo, vous avez trouvé la combinaison secrète en {nb_essai} tentatives !\n")
        return True
    else :
        print("\nVous n'avez pas trouvé la bonne combinaison,")
        lettre_commune = sorted(set(combi) & set(essai))
        print(f"il y a {len(lettre_commune)} lettres correctes :", *lettre_commune)  
        
        placement_lettres(combi, essai)

                
def jeu_mastermind(nb_lettres : int, liste_lettre : list) -> bool :
    
    print("\n-------------------------------------\nBienvenue dans le jeu du mastermind !\n-------------------------------------\n")
    print(f"Je choisis une combinaison de {nb_lettres} lettres différentes \nallant de 'A' à 'F', essayez de la deviner :)\n")

    combi_a_deviner = combi_secrete(nb_lettres, liste_lettre)
    nombre_de_vies = 10
        
    gagne = False
    
    for i in range(0, nombre_de_vies) :
        vie = nombre_de_vies - i
        nb_essai = nombre_de_vies - vie + 1
        
        print(f"Il vous reste {vie} essais,")
        essai = input("Entrez votre combinaison : ").upper()

        erreur = False
        for lettre in essai :
            if lettre not in liste_lettre :
                erreur = True
        if erreur == True :
            print("ERREUR : Au moins une lettre n'est pas comprise entre 'A' et 'F'\n")       
        elif len(essai) != nb_lettres :
            print(f"ERREUR : Assurez-vous d'entrer {nb_lettres} lettres\n")
        else :
            gagne = comparaison(combi_a_deviner, essai, nb_essai)
            if gagne :
                break
        
    if not gagne :
        print("\nVous avez perdu, la combinaison secrète était : ", *combi_a_deviner, "!\n")
            

if __name__ == "__main__":
    
    liste_lettre = ["A", "B", "C", "D", "E", "F"]
    nb_lettres_combinaison = 4
    jeu_mastermind(nb_lettres_combinaison, liste_lettre)
     """



#--------------- correction ------------------

def generer_combinaison(lettres: str, taille: int = 4) -> str:
    return ''.join(random.sample(lettres, k=taille))


def verification_saisie(lettres, combinaison_aleatoire):
    '''
    La vérification de la saisie se fait à plusieurs niveau
    1. On vérifie qu'il n'y ait pas de doublons en transformation la saisie en set
    2. On fait l'intersection du set avec le set des lettres valides
    Si tous les caractères saisies sont correctes, l'intersection devrait contenir 4 éléments
    3. On compare la longueur du set créé précédemment à la longueur de la combinaison à trouver12
    '''
    combinaison_utilisateur = input("Saisir une combinaison: ")
    while len(set(combinaison_utilisateur).intersection(set(lettres))) != len(combinaison_aleatoire):
        print("Saisie incorrecte !")
        combinaison_utilisateur = input("Saisir une combinaison: ")
    return combinaison_utilisateur


def comparaison(combinaison_aleatoire, combinaison_utilisateur):

    resultat = {}
    resultat['bien_place'] = 0
    resultat['mal_place'] = 0

    for pos in range(len(combinaison_aleatoire)):
        if combinaison_aleatoire[pos] == combinaison_utilisateur[pos]:
            resultat['bien_place'] += 1
        elif combinaison_utilisateur[pos] in combinaison_aleatoire:
            resultat['mal_place'] += 1

    return resultat


def main():
    lettres = ('A', 'B', 'C', 'D', 'E', 'F')

    print("  __  __   _   ___ _____ ___ ___ __  __ ___ _  _ ___  ")
    print(" |  \/  | /_\ / __|_   _| __| _ \  \/  |_ _| \| |   \\")
    print(" | |\/| |/ _ \ __ \ | | | _||   / |\/| || || .` | |) |")
    print(" |_|  |_/_/ \_\___/ |_| |___|_|_\_|  |_|___|_|\_|___/ ")

    combinaison_aleatoire = generer_combinaison(lettres)

    print(combinaison_aleatoire)

    for essai in range(1, 11):
        print('Essai n°', essai)
        combinaison_utilisateur = verification_saisie(
            lettres, combinaison_aleatoire)

        if combinaison_utilisateur == combinaison_aleatoire:
            print("Félicitations ! Vous avez gagné en ", essai, "essai(s)")
            exit()
        else:
            resultat = comparaison(combinaison_aleatoire,
                                   combinaison_utilisateur)
            print(
                f'Bien placées: {resultat["bien_place"]} Mal placées: {resultat["mal_place"]}')
    print("Vous avez perdu espèce de gros nullos")


if __name__ == '__main__':
    main()
