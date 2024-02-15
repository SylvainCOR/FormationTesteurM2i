#-------------if, elif, else-----------------

age_str = input("Quel est votre âge ? ")
age = int(age_str)

if age >= 18 :
    print("Vous êtes majeur")
elif 0 <= age < 18 :
    print("Vous êtes mineur")    
elif age > 60 :
    print("Vous êtes sénior")
else :
    print("Erreur : entrez une valeur positive")

    

