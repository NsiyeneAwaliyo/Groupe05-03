# Demander le texte et le mot à rechercher
texte = input("Entrez votre texte : ").lower()
mot = input("Entrez le mot à rechercher : ").lower()

# Compter les occurrences
occurrences = texte.split().count(mot)

# Afficher le résultat
print(f"Le mot '{mot}' apparaît {occurrences} fois dans le texte.")