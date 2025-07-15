# Programme de calcul de prime
anciennete = int(input("Entrez votre ancienneté (en années) : "))
performance = int(input("Entrez votre note de performance (1-5) : "))

if anciennete >= 5:
    if performance >= 4:
        prime = 2000
    else:
        prime = 1000
else:
    if performance >= 4:
        prime = 500
    else:
        prime = 0

# Affichage du résultat
if prime > 0:
    print(f"Félicitations ! Votre prime est de {prime} €")
else:
    print("Désolé, vous n'avez pas droit à une prime cette année")