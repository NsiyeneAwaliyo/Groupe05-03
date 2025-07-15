# Demander la phrase à l'utilisateur
phrase = input("Entrez un titre ou une phrase : ")

# Générer l'acronyme
acronyme = ''.join([mot[0].upper() for mot in phrase.split() if mot])  # if mot pour ignorer les mots vides

# Afficher le résultat
print(f"Acronyme généré : {acronyme}")