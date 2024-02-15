#-------------while, for, in, range-----------------

compteur = 11

while compteur > 0 :
    compteur -= 1
    print(f"Décompte : {compteur}")

    if compteur == 4:
        break
    # mots clé : break / continue / pass


print()
for i in range(0, 6):
    print(f"Compteur : {i}")
    
print()
for j in range(10, 30, 2):
    print(f"Pas de 2 : {j}")


import time
print()
for k in range(3, -1, -1):
    print(f"Décompte : {k}")
    time.sleep(1)
    
    if k == 0:
        print("TADAAAAA!!!")


