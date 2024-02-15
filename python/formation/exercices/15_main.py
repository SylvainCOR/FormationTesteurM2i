from adn import *

chaine_adn, sequence_adn = demander_adn()
chaine = chaine_adn.lower()
sequence = sequence_adn.lower()

saisie_adn(chaine)
saisie_adn(sequence)

print(f"Il y a {proportion(chaine, sequence)} % de concordance\n")