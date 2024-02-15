
def panne_moteur (liste) :
    return liste[1:] + [liste[0]]

def passe_en_tete (liste) :
    return [liste[1]] + [liste[0]] + liste[2:]

def sauve_honneur (liste) :
    return liste[0:-2] + [liste[-1]] + [liste[-2]]

def tir_blaster (liste) :
    return liste[1:]

def retour_inattendu (liste) :
    return liste + ["Yoshi"]

    
liste_concurrents = ['Mario', 'Luigi', 'Daisy', 'Wario', 'Bowser']

print("\n\t Liste des participants : \n     ", *liste_concurrents, "\n")
print("Quel dommage...", liste_concurrents[0], "subit une panne moteur !\nMaj des postions : \n  ", *panne_moteur (liste_concurrents), "\n")
liste_concurrents = panne_moteur (liste_concurrents)
print(liste_concurrents[1], "prends la tête de la course !\nMaj des postions : \n  ", *passe_en_tete (liste_concurrents), "\n")
liste_concurrents = passe_en_tete (liste_concurrents)
print(liste_concurrents[-1], "sauve l'honneur et double !", liste_concurrents[-2], "\nMaj des postions : \n  ", *sauve_honneur (liste_concurrents), "\n")
liste_concurrents = sauve_honneur (liste_concurrents)    
print("Oh non!", liste_concurrents[0], "se prends un tir de blaster !\nMaj des postions : \n  ", *tir_blaster (liste_concurrents), "\n")
liste_concurrents = tir_blaster (liste_concurrents)  
print("Mais qui est cet intrus sur la piste !?\nMaj des postions : \n  ", *retour_inattendu (liste_concurrents), "\n")
liste_concurrents = retour_inattendu (liste_concurrents)  

    