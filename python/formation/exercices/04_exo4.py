#--------- Etat de l'eau ----------

temp_str = input("Quelle est la température de l'eau ? ")
temp = int(temp_str)

if temp > 100 :
    etat = "gazeux"
elif 0 <= temp <= 100 :
    etat = "liquide"  
else :
    etat = "solide"

print(f"D'après les données recueillies, l'eau se trouve à l'état {etat}.")


########## Correction ##########

# Ecriture ternaire
print("Solide" if (temp < 0) else "Liquide" if (temp <= 100) else "Gazeux")

