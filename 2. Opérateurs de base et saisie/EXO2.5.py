# Convertisseur de devises USD vers EUR, XOF, GBP

# Taux de conversion (fixes)
TAUX_EUR = 0.93   # 1 USD = 0.93 EUR
TAUX_XOF = 610    # 1 USD = 610 XOF
TAUX_GBP = 0.79   # 1 USD = 0.79 GBP

# Demander le montant en dollars
montant_usd = float(input("Entrez le montant en USD : $"))

# Calculer les conversions
montant_eur = montant_usd * TAUX_EUR
montant_xof = montant_usd * TAUX_XOF
montant_gbp = montant_usd * TAUX_GBP

# Afficher les résultats
print("\nRésultats de conversion :")
print(f"${montant_usd:.2f} USD = {montant_eur:.2f} EUR")
print(f"${montant_usd:.2f} USD = {montant_xof:.2f} XOF")
print(f"${montant_usd:.2f} USD = {montant_gbp:.2f} GBP")