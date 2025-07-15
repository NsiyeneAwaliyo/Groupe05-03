print("Entrez vos notes une par une (entre 0 et 20). Saisissez -1 pour terminer.")

notes = []
while True:
    saisie = input("Note (ou -1 pour terminer) : ")
    
    # Vérifier si l'utilisateur veut quitter
    if saisie == "-1":
        break
        
    try:
        note = float(saisie)
        # Vérifier si la note est valide (entre 0 et 20)
        if 0 <= note <= 20:
            notes.append(note)
        else:
            print("Erreur : la note doit être entre 0 et 20.")
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide.")

# Calculer et afficher la moyenne si au moins une note a été saisie
if len(notes) > 0:
    moyenne = sum(notes) / len(notes)
    print(f"\nNombre de notes saisies : {len(notes)}")
    print(f"Moyenne : {moyenne:.2f}/20")  # Arrondi à 2 décimales
else:
    print("\nAucune note valide n'a été saisie.")