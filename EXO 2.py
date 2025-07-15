# Demander les informations du produit
print("Création de la fiche produit\n" + "="*30)
nom = input("Nom du produit : ")
prix = float(input("Prix initial (€) : "))
stock = int(input("Quantité en stock : "))
remise = float(input("Remise (%) : "))

# Calculer le prix après remise
prix_final = prix * (1 - remise / 100)

# Afficher la fiche produit
print("\nFICHE PRODUIT")
print("-"*30)
print(f"Nom: {nom}")
print(f"Prix initial: {prix:.2f}€")
print(f"Remise: {remise}%")
print(f"Prix après remise: {prix_final:.2f}€")
print(f"Stock disponible: {stock} unités")
print("-"*30)
print(f"Économie: {prix - prix_final:.2f}€")