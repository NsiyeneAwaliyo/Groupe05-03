# Demander la phrase à l'utilisateur
phrase = input("Entrez une phrase : ")

# Séparer les mots et compter ceux avec plus de 5 lettres
mots = phrase.split()
nb_mots_long = sum(1 for mot in mots if len(mot) > 5)

# Afficher le résultat
print(f"Nombre de mots avec plus de 5 lettres : {nb_mots_long}")
