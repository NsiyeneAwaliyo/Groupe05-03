# Demander la valeur du panier
montant_panier = float(input("Entrez le montant de votre panier (en €) : "))

# Calculer les frais de livraison
if montant_panier >= 100:
    frais_livraison = 0
    message_livraison = "Livraison gratuite !"
elif montant_panier >= 50:
    frais_livraison = 5
    message_livraison = "Frais de livraison : 5 €"
else:
    frais_livraison = 10
    message_livraison = "Frais de livraison : 10 €"

# Calculer le total
total = montant_panier + frais_livraison

# Afficher le détail
print("\nRécapitulatif de commande :")
print(f"Montant du panier : {montant_panier:.2f} €")
print(message_livraison)
print(f"Total à payer : {total:.2f} €")