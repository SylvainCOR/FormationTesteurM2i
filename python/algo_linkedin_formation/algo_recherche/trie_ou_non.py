#-------------Déterminer si le tableau est trié-----------------

def est_trie(tab):
    
    for i in range(0, len(tab) - 1) :
        if tab[i] > tab[i + 1] :
            return False
    return True

def est_trie_2(tab) :
    
    return all(tab[i] <= tab[i + 1] for i in range(len(tab) - 1))
    
liste1 = [5, 2, 0, 8, 3, 9, 1, 6, 4, 7]
liste2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(est_trie(liste1))
print(est_trie(liste2))
print()
print(est_trie_2(liste1))
print(est_trie_2(liste2))