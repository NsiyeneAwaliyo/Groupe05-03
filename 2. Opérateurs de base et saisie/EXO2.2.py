# Demander un nombre entier à l'utilisateur
nombre = int(input("Entrez un nombre entier : "))

# Vérifier si le nombre est divisible par 3 et 5
if nombre % 3 == 0 and nombre % 5 == 0:
    print(f"{nombre} est divisible par 3 et 5.")
else:
    print(f"{nombre} n'est pas divisible par 3 et 5.")