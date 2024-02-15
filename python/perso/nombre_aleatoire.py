import random

def jeu_de_devinette():
    print("Bienvenue dans le jeu de devinette !")
    print("Je choisis un nombre entre 1 et 100, essayez de le deviner.")

    nombre_a_deviner = random.randint(1, 100)
    nombre_d_essais = 0

    while True:
        try:
            devine = int(input("Entrez votre réponse : "))
            nombre_d_essais += 1

            if devine == nombre_a_deviner:
                print(f"Bravo, vous avez trouvé le nombre en {nombre_d_essais} essais !")
                break
            elif devine < nombre_a_deviner:
                print("Le nombre est plus grand. Essayez encore.")
            else:
                print("Le nombre est plus petit. Essayez encore.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    jeu_de_devinette()
