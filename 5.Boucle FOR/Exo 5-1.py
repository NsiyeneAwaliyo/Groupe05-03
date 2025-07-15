# Programme de table de multiplication
nombre = int(input("Entrez un nombre : "))

print(f"\nTable de multiplication de {nombre} :")
print("-" * 30)  # Ligne de séparation

for i in range(1, 13):
    print(f"{nombre} × {i:2} = {nombre * i:3}")

print("-" * 30)  # Ligne de séparation