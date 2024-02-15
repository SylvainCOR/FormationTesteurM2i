#------------Stocker adresses-------------------

def menu() :
    
    while True :
        # affiche le menu tant que le choix de l'utilisateur n'est pas correct
        print("""\nMenu :
            1. Voir les adresses            2. Ajouter une adresse
            3. Editer une adresse           4. Supprimer une adresse            
            5. Quitter le programme""")
        choix = input("Votre choix : ")

        if choix in "12345" :
            return choix
        else :
            print("Erreur! Le choix doit être compris entre 1 et 5")


def afficher_adresses(liste) :
    
    x = 1
    for dict in liste :
        # affiche la position de l'adresse dans la liste
        print("----------------------------------------------------------------------")
        print(f"\t\t\t\tADRESSE {x}")
        print("----------------------------------------------------------------------")
                
        # affiche l'adresse lignes par lignes
        for k, v in dict.items() :
            print(f"\t -> {k} : {v}")
        x += 1


def ajouter_adresse() :
    
    # initialisation du dictionnaire 
    dict = {"Numéro de voie" : "",
          "Complément" : "",
          "Intitulé de voie" : "",
          "Commune" : "",
          "Code Postal" : ""
          }
    # demande les valeurs pour chaque clés
    for k in dict.keys() :
        dict[k] = input(f"Renseignez : {k} : ")
        
    return dict # renvoie un dictionnaire complété


def modifier_adresse(liste) :
    
    # récupère la position de l'adresse à modifier
    x = int(input("\nNuméro de l'adresse à modifier : "))
    if x in range(1, len(liste) + 1) :
        print(f"Modification de l'adresse : {x}\n")
        dict_temp = ajouter_adresse()
        liste[x - 1] = dict_temp
    else :
        print("ERREUR ! le numéro d'adresse est incorrect")
        modifier_adresse(liste) # recommence la fonction si la position est incorrecte


def supprimer_adresse(liste) :
    
    # récupère la position de l'adresse à modifier
    x = int(input("\nNuméro de l'adresse à supprimer : "))
    if x in range(1, len(liste) + 1)  :
        print(f"Suppression de l'adresse : {x}\n")
        del liste[x - 1]
    else :
        print("ERREUR ! le numéro d'adresse est incorrect")
        supprimer_adresse(liste) # recommence la fonction si la position est incorrecte  


def affichage(liste) :

    while True :
        # recupère le choix et affiche le sous menu correspondant
        choix = menu()

        match choix :
            case "1" :
                afficher_adresses(liste)
            case "2" :
                dict = ajouter_adresse()
                liste.append(dict)
            case "3" :
                modifier_adresse(liste)
            case "4" :
                supprimer_adresse(liste)
            case "5" :
                print("Au revoir !")
                exit()


liste = []
affichage(liste)
