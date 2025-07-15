# Demander une phrase à l'utilisateur
phrase = input("Veuillez entrer une phrase : ")

# Séparer les mots de la phrase
mots = phrase.split()

# Créer une liste avec un mot sur deux
mot_sur_deux = mots[::2]

# Afficher le résultat
print("Liste avec un mot sur deux :", mot_sur_deux)