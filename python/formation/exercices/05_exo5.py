#--------- Vérification du profil ----------

age = int(input("Quel est votre âge ? "))

if age < 30 :
    print("Trop jeune, au revoir!")
    exit()
    
salaire = int(input("Prétention salariale ? "))
if salaire > 40000 :
    print("Trop gourmand, au revoir!")
    exit()

exp = int(input("Année(s) d'expérience ? "))
if exp < 5 :
    print("Inexpérimenté, au revoir!")
    exit()
    
else :
    print("Félicitations! Votre profil est éligible.")

            

