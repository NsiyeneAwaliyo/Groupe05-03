# Demander à l'utilisateur de saisir deux nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Calculer les différentes opérations
somme = nombre1 + nombre2
difference = nombre1 - nombre2
produit = nombre1 * nombre2

# Division réelle (on vérifie que le deuxième nombre n'est pas zéro)
if nombre2 != 0:
    quotient_reel = nombre1 / nombre2
else:
    quotient_reel = "Indéfini (division par zéro)"

# Division entière et modulo (on vérifie aussi la division par zéro)
if nombre2 != 0:
    division_entiere = nombre1 // nombre2
    modulo = nombre1 % nombre2
else:
    division_entiere = "Indéfini (division par zéro)"
    modulo = "Indéfini (division par zéro)"

# Afficher les résultats
print(f"\nRésultats :")
print(f"Somme : {nombre1} + {nombre2} = {somme}")
print(f"Différence : {nombre1} - {nombre2} = {difference}")
print(f"Produit : {nombre1} * {nombre2} = {produit}")
print(f"Quotient réel : {nombre1} / {nombre2} = {quotient_reel}")
print(f"Division entière : {nombre1} // {nombre2} = {division_entiere}")
print(f"Reste (modulo) : {nombre1} % {nombre2} = {modulo}")