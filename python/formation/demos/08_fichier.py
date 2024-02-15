import os

file_path = "./python/formation/demos/fichier.txt"

if os.path.exists(file_path) :
    file = open(file_path, "r", encoding="UTF-8")
    print(file.readline())
    file.close()
else :
    file = open(file_path, "w", encoding="UTF-8")
    file.write("J'écris dans mon fichier .txt\n")
    file.close()

with open(file_path, "r", encoding="UTF-8") as mon_fichier :
    print(type(mon_fichier))


