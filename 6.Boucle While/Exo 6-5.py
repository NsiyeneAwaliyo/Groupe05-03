# Demander un nombre entier positif
while True:
    try:
        n = int(input("Entrez un nombre entier positif : "))
        if n >= 0:
            break
        else:
            print("Erreur : le nombre doit être positif.")
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier valide.")

# Calcul de la factorielle
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

# Affichage du résultat
print(f"La factorielle de {n} est : {factorial}")