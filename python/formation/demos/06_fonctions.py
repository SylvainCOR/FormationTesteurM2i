def hello_world() :
    print("hello world")
    
hello_world()

def bonjour(nom : str) :
    print("Bonjour", nom)

bonjour("Toto")

def addition(a, b) :
    print("Addition :")
    return a + b

print(addition(1, 5))

resultat = addition(10, 5)
print(resultat)

a = 10

def test() :
    global a
    a = 300
    print(a)

test()
print(a)

def test2() :
    a = 20
    print(a)

test2()
print(a)


