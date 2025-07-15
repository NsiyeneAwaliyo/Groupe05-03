# Demander la liste à l'utilisateur
elements = input("Entrez des éléments séparés par des espaces : ").split()

# Afficher chaque élément avec son indice
print("\nÉléments avec leur indice :")
for indice, element in enumerate(elements):
    print(f"{indice} : {element}")