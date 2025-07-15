# Demander l'adresse email
email = input("Entrez votre adresse email : ")

# Vérifier la fin de l'adresse
if email.endswith("@gmail.com"):
    print("Adresse Gmail valide !")
else:
    print("Cette adresse n'est pas une adresse Gmail valide.")