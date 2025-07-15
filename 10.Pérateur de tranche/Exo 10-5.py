# Demander à l'utilisateur d'entrer des nombres séparés par des espaces
entree = input("Entrez une liste de nombres séparés par des espaces : ")

# Convertir l'entrée en une liste de nombres (float)
liste_nombres = list(map(float, entree.split()))

# Extraire les éléments aux indices pairs
indices_pairs = liste_nombres[::2]

# Afficher le résultat
print("Éléments aux indices pairs :", indices_pairs)