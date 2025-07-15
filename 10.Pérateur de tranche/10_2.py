# Demander la liste à l'utilisateur
elements = input("Entrez des éléments séparés par des espaces : ").split()

# Inverser la liste avec slicing
liste_inversee = elements[::-1]

# Afficher le résultat
print("Liste inversée :", liste_inversee)
