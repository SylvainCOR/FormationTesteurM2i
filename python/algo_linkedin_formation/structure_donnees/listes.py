#----------liste numerique simple-----------

maliste = [11, 28, 12, 5, 64, 23, 87, 12, 23]
print(maliste)
item0 = maliste[0]
print(item0)
maliste[1] = 100
print(maliste)

sum0 = 0
for i in range(len(maliste)):
    sum0 = sum0 + maliste[i]
print(sum0)

j = 0
sum1 = 0
while j < (len(maliste)):
    sum1 = sum1 + maliste[j]
    j = j + 1
print(sum1)


#----------liste chainée-----------

class Noeud(object):
    def __init__(self, value):
        self.value = value
        self.noeud_suivant = None
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
    def get_noeud_suivant(self):
        return self.noeud_suivant      

    def set_noeud_suivant(self, noeud_suivant):
        self.noeud_suivant = noeud_suivant        

class ListeChainee(object):
    def __init__(self, head = None):
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count

    def insert(self, value):
        new_noeud = Noeud(value)
        new_noeud.set_noeud_suivant(self.head)
        self.head = new_noeud
        self.count = self.count + 1

    def print_liste(self):
        print("Affichage des élémeents de la liste : ")
        noeud = self.head
        while noeud != None :
            print("Noeud : ", noeud.get_value())
            noeud = noeud.get_noeud_suivant()

# creation de la liste chainée
maliste = ListeChainee()

# insertion de nouveaux éléments
for i in range(10):
    maliste.insert(i)

# affichage de tous les éléments de la liste
maliste.print_liste()

# recherche du nombre d'elements dans la liste
print("Le nombre d'éléments dans la liste : ", maliste.get_count())
