#-------------Pliage du papier--------------

papier = 0.0001
pliage = 0

while papier < 400 :
    papier *= 2
    pliage +=1
    # print(papier)

print(f"Nombre de pliages nécessaires : {pliage}")


#-------------Dépliage du papier--------------

papier = 400
depliage = 0

while papier >= 0.0001 :
    papier /= 2
    depliage +=1
    # print(papier)

print(f"Nombre de dépliages nécessaires : {depliage}")


