# Demander la phrase et le mot à remplacer
phrase = input("Entrez une phrase : ")
mot_a_remplacer = input("Entrez le mot à masquer : ")

# Créer le masque d'astérisques
masque = '*' * len(mot_a_remplacer)

# Remplacer toutes les occurrences (insensible à la casse)
phrase_modifiee = phrase.replace(mot_a_remplacer, masque)

# Afficher le résultat
print("\nPhrase modifiée :")
print(phrase_modifiee)