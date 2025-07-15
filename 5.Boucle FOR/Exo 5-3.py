# Variante avec accès par indice
chaine = input("Entrez une chaîne : ")
inverse = ""

for i in range(len(chaine)-1, -1, -1):  # Parcourt du dernier au premier indice
    inverse += chaine[i]

print("Version inversée :", inverse)