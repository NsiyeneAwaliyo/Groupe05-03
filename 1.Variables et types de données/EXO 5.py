# Demander la distance en km et le temps en heures
distance_km = float(input("Entrez la distance en kilomètres : "))
temps_heures = float(input("Entrez le temps en heures : "))

# Calculer la vitesse en km/h
vitesse_kmh = distance_km / temps_heures

# Convertir la distance en mètres et le temps en secondes
distance_m = distance_km * 1000  # 1 km = 1000 m
temps_s = temps_heures * 3600    # 1 heure = 3600 secondes

# Calculer la vitesse en m/s
vitesse_ms = distance_m / temps_s

# Afficher les résultats
print(f"Vitesse moyenne : {vitesse_kmh:.2f} km/h")
print(f"Vitesse : {vitesse_ms:.2f} m/s")