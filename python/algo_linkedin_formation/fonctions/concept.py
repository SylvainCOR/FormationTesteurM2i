#-------------Notions de base-----------------

def mafonction1():
    print("Je suis la fonction 'mafonction1'")
    
def mafonction2(n):
    return n * n

def mafonction3(n, m):
    return n * m

mafonction1()

result = mafonction2(5)
print("Résultat de mafonction2 :", result)

print(f"Résultat de mafonction3 : {mafonction3(10, 5)}")


#-------------Découpage-----------------

def perimetre_carre(x):
    print(f"Le périmètre du carré est de {x * 4} m")

def surface_carre(x):
    print(f"La surface du carré est de {x * x} m^2")

def volume_carre(x):
    print(f"Le volume du carré est de {x ** 3} m^3")

cote = 3
perimetre_carre(cote)
surface_carre(cote)
volume_carre(cote)


#-------------Paramètre de fonction-----------------

def mafonction(n):
    n = 2
    return n

n = 10
result = mafonction(n)

print("Résultat de l'exécution de la fonction :", result)
print("La valeur de n dans le programme appelant est :", n)

