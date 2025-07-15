MOT_DE_PASSE_CORRECT = "Python2025"

while True:
    saisie = input("Entrez le mot de passe : ")
    
    if saisie == MOT_DE_PASSE_CORRECT:
        print("Accès autorisé !")
        break
    else:
        print("Mot de passe incorrect. Veuillez réessayer.")