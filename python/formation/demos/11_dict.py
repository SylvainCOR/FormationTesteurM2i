mon_dict = {}

mon_dict = {
    "clé1" : "valeur 1",
    2 : 2,
    True : False,
    "contacts" : ["toto", "titi"]
    }

print(mon_dict["contacts"])

mon_dict["blabla"] = "texte"
print(mon_dict)

mon_dict["clé1"] = "modif"
print(mon_dict)

del mon_dict["blabla"] 
print(mon_dict)

print()
print(mon_dict.values())
for v in mon_dict.values() :
    print(v)
for k in mon_dict.keys() :
    print(k)   

print(mon_dict.items())
for clé, valeur in mon_dict.items() :
    print(f"clé = {clé} et valeur = {valeur}")   

mon_dict.pop("contacts")
print(mon_dict)

mon_dict.update({25 : "test", "M" : True})
print(mon_dict)
print()
print(*mon_dict)