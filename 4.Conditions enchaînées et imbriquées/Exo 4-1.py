# Programme de calcul de tarif personnalisé
age = int(input("Entrez votre âge : "))
situation = input("Entrez votre situation (étudiant/salarié/retraité) : ").lower()

# Détermination du tarif
if age < 18:
    tarif = 5
elif 18 <= age <= 25:
    if situation == "étudiant":
        tarif = 6
    elif situation == "salarié":
        tarif = 8
    else:
        tarif = 10  # Cas par défaut pour cette tranche d'âge
else:  # plus de 25 ans
    if situation == "retraité":
        tarif = 7
    else:
        tarif = 10

# Affichage du résultat
print(f"\nÀ {age} ans ({situation}), votre tarif est de {tarif} €")