# Demander l'âge et le pays
age = int(input("Entrez votre âge : "))
pays = input("Entrez votre pays : ").strip().title()  # Normalise la saisie

# Vérifier les conditions d'inscription
if age >= 18 and (pays == "Congo" or pays == "Cameroun"):
    print("Félicitations ! Vous pouvez vous inscrire au programme.")
else:
    print("Désolé, vous ne remplissez pas les conditions d'inscription.")
    if age < 18:
        print("- Vous devez avoir au moins 18 ans.")
    if pays != "Congo" and pays != "Cameroun":
        print("- Vous devez venir du Congo ou du Cameroun.")
