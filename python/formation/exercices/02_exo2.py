#--------- Calcul du colume d'un cône droit ----------

import math

ray = input("Saisir le rayon du cône (en m) : ")
high = input("Saisir la hauteur du cône (en m): ")

try:
    volume = (1/3) * math.pi * (int(ray) ** 2) * int(high)
    print(f"Le volume du cône droit est  de {round(volume,2)} m^3")
except:
    print("Les valeurs entrées doivent être numériques") 


########## Correction ##########

from math import pi

hauteur = float(input("Saisir la hauteur d'un cône : "))
rayon = float(input("Saisir le rayon d'un cône : "))
volume = (pi*rayon**2*hauteur)/3

print(f"volume : {round(volume, 2)}")
