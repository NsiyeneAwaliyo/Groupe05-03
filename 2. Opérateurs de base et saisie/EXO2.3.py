# Saisie du montant HT et du taux de TVA
montant_ht = float(input("Entrez le montant HT (en euros) : "))
taux_tva = float(input("Entrez le taux de TVA (en %) : "))

# Calcul du montant TTC
montant_ttc = montant_ht * (1 + taux_tva / 100)

# Affichage du résultat
print(f"\nRésultat :")
print(f"Montant HT : {montant_ht:.2f} €")
print(f"TVA ({taux_tva}%) : {montant_ht * taux_tva / 100:.2f} €")
print(f"Montant TTC : {montant_ttc:.2f} €")