#-------------Accroissement de population--------------

pop_init = int(input("Entrez une population initiale : "))
tx_acc = int(input("Entrez le taux d'accoissement (en %) : "))
pop_finale = int(input("Entrez la population visée : "))

annee = 0

while pop_init <= pop_finale :
    pop_init *= 1 + (tx_acc/100)
    # print(round(pop_init, 2))
    annee += 1

print(f"\nLa population visée sera atteinte dans {annee} ans\n")

