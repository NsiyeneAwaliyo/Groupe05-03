# Programme de comptage de voyelles
mots = input("Entrez des mots séparés par des espaces : ").split()
voyelles = {'a', 'e', 'i', 'o', 'u', 'y'}  # On peut ajouter les majuscules si besoin

total_voyelles = 0

for mot in mots:
    for lettre in mot.lower():  # Conversion en minuscule pour uniformiser
        if lettre in voyelles:
            total_voyelles += 1

print(f"Nombre total de voyelles : {total_voyelles}")