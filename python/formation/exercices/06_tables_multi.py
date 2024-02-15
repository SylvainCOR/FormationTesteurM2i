#-------------Afficher tables de 1 à N.N--------------

import time

N = int(input("Entrez un entier > 0 : "))

for i in range(10) :
    print(f"{(i + 1):4}", end="     ")
print("\n__________________________________________________________________________________________\n")

for j in range(1, N+1) :
    time.sleep(0.3)
    k = 1
    while k <= 10 :
        print(f"{(k * j):4}", end="     ")
        k += 1
    print("\n")



