while True:
    mot = input("Entrez un mot d'au moins 5 lettres : ")
    if len(mot) >= 5:
        break
    print("Erreur : le mot doit contenir au moins 5 lettres. Veuillez réessayer.")

partie_centrale = mot[2:-2]
print(f"La partie centrale du mot est : {partie_centrale}")