# Création d'une matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Affichage 1 - Simple
print("Affichage élément par élément :")
for i in range(3):  # Pour chaque ligne
    for j in range(3):  # Pour chaque colonne
        print(f"matrice[{i}][{j}] = {matrice[i][j]}")

# Affichage 2 - Visuel matriciel
print("\nAffichage matriciel :")
for ligne in matrice:
    print(ligne)

# Affichage 3 - Formaté avec séparateurs
print("\nAffichage formaté :")
for ligne in matrice:
    print("|", end=" ")
    for element in ligne:
        print(element, end=" | ")
    print()  # Retour à la ligne