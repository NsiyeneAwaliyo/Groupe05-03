

try:
    heures = abs(int(input("Nombre d'heures : ")))
    minutes = abs(int(input("Nombre de minutes : ")))
    secondes = abs(int(input("Nombre de secondes : ")))
    
    # Ajustement si minutes ou secondes > 60
    minutes += secondes // 60
    secondes = secondes % 60
    heures += minutes // 60
    minutes = minutes % 60
    
    total_secondes = (heures * 3600) + (minutes * 60) + secondes
    
    print(f"\nDurée convertie : {heures}h {minutes}min {secondes}s = {total_secondes} secondes")
except ValueError:
    print("Erreur : Veuillez entrer des nombres entiers valides.")