# Création de la liste des carrés
carres = [n**2 for n in range(1, 21)]  # Compréhension de liste

# Filtrage et affichage des carrés > 100
print("Carrés supérieurs à 100 :")
for carre in carres:
    if carre > 100:
        print(carre)