#-------------Sapin d'étoiles--------------

x = int(input("Entrez la hauteur du triangle : "))

nb_espace = 0
nb_etoile = 0

for i in range(1, x + 1):
    nb_espace = " " * (x - i)
    nb_etoile = "*" * (i * 2 - 1)
    print(f"{nb_espace}{nb_etoile}{nb_espace}")

    
   