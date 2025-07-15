# Demander la liste à l'utilisateur
entree = input("Entrez des éléments séparés par des espaces : ")

# Convertir en liste (en conservant le type str pour tous les éléments)
liste_originale = entree.split()

# Méthode 1: Utilisation d'un set (non ordonné)
valeurs_uniques = list(set(liste_originale))
print("\nMéthode avec set (non ordonné):")
print("Liste originale:", liste_originale)
print("Valeurs uniques:", valeurs_uniques)

# Méthode 2: Conservation de l'ordre d'apparition
valeurs_uniques_ordonnees = []
for element in liste_originale:
    if element not in valeurs_uniques_ordonnees:
        valeurs_uniques_ordonnees.append(element)

print("\nMéthode avec ordre conservé:")
print("Liste originale:", liste_originale)
print("Valeurs uniques:", valeurs_uniques_ordonnees)