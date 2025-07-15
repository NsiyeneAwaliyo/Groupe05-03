# Demander le texte à l'utilisateur
texte = input("Entrez votre texte : ")

# 1. Retirer les espaces en trop (début/fin et multiples)
texte_propre = ' '.join(texte.strip().split())

# 2. Convertir en minuscules
texte_minuscule = texte_propre.lower()

# 3. Remplacer les points par des points d'exclamation
texte_final = texte_minuscule.replace('.', '!')

# Afficher le résultat
print("\nTexte transformé :")
print(texte_final)