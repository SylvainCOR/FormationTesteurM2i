#-------------Compte à rebours-----------------

import time

def countdown(x):
    if x == 0 :
        time.sleep(1)
        print("Décollage !\n")
        return
    else :
        time.sleep(1)
        print(x)
        countdown(x - 1)

print("Allumage . . . \n     Démarrage du compte à rebours . . . ")
time.sleep(1)
countdown(5)
    