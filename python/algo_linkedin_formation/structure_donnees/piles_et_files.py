#----------Exemple de pile-----------

# création d'une pile
stack = []

# ajouter des valeurs
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

# affichage de la liste
print(stack)

# suppression d'un élément de la pile
item = stack.pop()
print("La valeur supprimée est :", item)

# affichage des éléments restants
print(stack)


#----------Exemple de file-----------
from collections import deque

# création d'une file
queue = deque()

# ajouter des valeurs
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# affichage de la liste
print(queue)

# suppression d'un élément de la pile
item = queue.popleft()
print("La valeur supprimée est :", item)

# affichage des éléments restants
print(queue)

