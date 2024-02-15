
p = input("Quel est votre prénom ? ")
n = input("Quel est votre nom ? ")

prenom = p[0].upper() + p[1:].lower()
nom = n.upper()

print(f"Bonjour, M. ou Mme {prenom} {nom}")


########## Correction ##########

nom = input("Votre nom ? ")
prenom = input("Votre prénom ? ")

print(f"Bonjour, M. ou Mme {prenom.title()} {nom.upper()}")