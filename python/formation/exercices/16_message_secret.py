import os, time


file_path = "./python/formation/exercices/fichier_secret.txt"
nouveau_secret = ""

#------------------------Fonctions--------------------------------------

def afficher_menu(secret = "") :
    global nouveau_secret
    
    reponse = str(input("\nSouhaitez-vous : \n" + 
                        "\t1) Voir le secret ?\n" + 
                        "\t2) Modifier le secret ?\n" + 
                        "\t3) Quitter le programme ?\n\n" + 
                        "Entrez votre choix : "))
    
    if reponse == "1" :
        print(secret)
        time.sleep(2)
        afficher_menu()
        
    elif reponse == "2" :
        nouveau_secret = input("\nQuel est le nouveau secret ? ")
        print("\nLe nouveau secret est bien pris en compte\n" +
                "et sera enregistré à la fermeture du programme !")
        afficher_menu()
        
    elif reponse == "3" :
        print("\nAu revoir !\n")
        if nouveau_secret != "" :
            file = open(file_path, "w", encoding="UTF-8")
            file.write(nouveau_secret + "\n")
            file.close
        return 
    else :
        print("Erreur! Entrez une réponse correcte (entre 1 et 3)")
        afficher_menu() 

def nouveau_fichier() :
    nouveau_secret = input("\nEntrez le nouveau secret : ")
    file = open(file_path, "w", encoding="UTF-8")
    file.write(nouveau_secret + "\n")
    file.close()
    print("\nFichier secret créé avec succès !")
    return ("\n" + nouveau_secret) 



#------------------------Programme--------------------------------------

if os.path.exists(file_path) :
    
    file = open(file_path, "r", encoding="UTF-8")
    message_secret = ("\n" + file.readline())
    file.close
    
    afficher_menu(message_secret)
else :
    saisie = nouveau_fichier()
    afficher_menu(saisie)



################ CORRECTION #################
"""
def show_menu() :
    while True :
        print('''Faites votre choix :
              1. Voir le secret
              2. Modifier le secret
              3. Quitter le programme''')
        choix = input("Votre choix : ")
        
        if choix in"123" :
            return choix
        else :
            print("Erreur! \n\n")

def lire_fichier(path) :
    file = open(path, "r", encoding="UTF-8")
    texte_fichier = file.read()
    file.close()
    return texte_fichier

def ecrire_fichier(path, texte):
    file = open(path, "w", encoding="UTF-8")
    file.write(texte)
    file.close()
    
def main() :
    file_path = "./projets_python/m2i_formation/exercices/16_message_secret/fichier_secret.txt"
    
    if os.path.exists(file_path) :
        secret = lire_fichier
    else :
        print("Secret n'existe pas !")
        secret = input("Veuillez saisir un premier secret : ")
    
    while True :
        choix = show_menu()
        
        match choix :
            case "1" :
                print("Voici le secret : ", secret)
            case "2" : 
                secret = input("Veuillez saisir le nouveau secret : ")
            case "3" :
                print("Fin du programme ")
                ecrire_fichier(file_path, secret)
                break
            
main() """