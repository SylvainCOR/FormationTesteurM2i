#-------------Compter lettre a--------------

def a_boucle(str) :
    str_lower = str.lower()
    resultat = 0
    for i in range(len(str_lower)) :
        if str_lower[i] == "a" :
            resultat += 1
    return resultat

print(a_boucle("BArBARa"))


def a_count(str) :
    str_lower = str.lower()
    resultat = str_lower.count("a")
    return resultat

print(a_count("Abba"))


