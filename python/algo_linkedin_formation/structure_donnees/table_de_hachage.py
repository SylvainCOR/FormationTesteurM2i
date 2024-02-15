#----------Exemple de table de hachage-----------

# création d'un dictionnaire en 1 seule instruction
dict1 = dict({"clé1" : 1, "clé2" : 2, "clé3" : "Hello"})
print(dict1)

# création d'un dictionnaire élément par élément
dict2 = {}
dict2["clé1"] = 1
dict2["clé2"] = 2
dict2["clé3"] = 3
dict2["clé4"] = 4
print(dict2)

dict2["clé2"] = "two"
print(dict2)
