# Demander la note à l'utilisateur
note = float(input("Entrez votre note sur 100 : "))

# Vérifier la validité de la note
if note < 0 or note > 100:
    print("Erreur : la note doit être comprise entre 0 et 100.")
else:
    # Attribuer la mention en fonction de la note
    if note >= 90:
        mention = "Excellent"
    elif note >= 75:
        mention = "Très Bien"
    elif note >= 60:
        mention = "Bien"
    elif note >= 50:
        mention = "Passable"
    else:
        mention = "Insuffisant"
    
    # Afficher le résultat
    print(f"Note : {note}/100 - Mention : {mention}")