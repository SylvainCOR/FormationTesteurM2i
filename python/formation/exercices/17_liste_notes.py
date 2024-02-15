#-----------------Notes min/max/moyenne------------------------

def min_max(liste) :
    
    # initialise les variables min et max
    max = liste[0]  
    min = liste[0]
    
    for i in range(len(liste)) :    
        # recherche du min et du max dans la liste
        if max < liste[i] :
            max = liste[i]
        if min > liste[i] :
            min = liste[i]

    return(min, max) # renvoie les valeurs de min et max


def ajout_note(liste) :
    
    while True :
        # demande une valeur tant qu'on est dans le programme
        note = float(input("Entrez la note obtenue (ou -1 pour quitter) : "))

        if 0 <= note <= 20 :
            # ajoute la valeur saisie dans la liste
            liste.append(note)
        elif note == -1 :
            # quitte la boucle et la fonction
            break
        else :
            print("Erreur ! Veuillez entrer une note entre 0 et 20")

    if liste == [] :
        print("La liste est vide, renseignez au moins une note")
        ajout_note(liste)
    
    return liste # renvoie une liste de notes


def menu() :
    
    while True :
        # affiche le menu tant que le choix de l'utilisateur n'est pas correct
        print("""Afficher :
            1. Note minimale            2. Note maximale
            3. Moyenne de la classe     4. Liste des notes            
            5. Ajouter des notes        6. Quitter le programme""")
        choix = input("Votre choix : ")

        if choix in "123456" :
            return choix
        else :
            print("Erreur! Lechoix doit être compris entre 1 et 6 \n\n")


def affichage (liste) :
    
    # remplissage de la liste
    ajout_note(liste)
    
    while True :
        # recupère le choix et affiche le sous menu correspondant
        
        choix = menu()
        min, max =  min_max(liste)
        
        match choix :
            case "1" :
                print("La note minimale est : ", min, "\n")
            case "2" :
                print("La note maximale est : ", max, "\n")
            case "3" :
                moyenne = sum(liste) / len(liste)
                print("La moyenne est de : ", round(moyenne, 2), "\n")
            case "4" :
                # conversion de la liste int en liste str (pour appliquer .join)
                liste_str = [str(i) for i in liste]
                print("Liste des notes : ", ", ".join(liste_str), "\n")
            case "5" :
                ajout_note(liste)             
            case "6" :
                print("Au revoir !")
                exit()


liste_notes = []
affichage(liste_notes)

