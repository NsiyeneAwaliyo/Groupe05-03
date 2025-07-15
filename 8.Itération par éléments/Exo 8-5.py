# Demander le texte à l'utilisateur
texte = input("Entrez un texte : ")

# Définir les voyelles (minuscules et majuscules)
voyelles = "aeiouyAEIOUYéèêëàâäîïôöùûüÉÈÊËÀÂÄÎÏÔÖÙÛÜ"

# Extraire et afficher les consonnes
consonnes = [caractere for caractere in texte if caractere.isalpha() and caractere not in voyelles]
print("".join(consonnes))