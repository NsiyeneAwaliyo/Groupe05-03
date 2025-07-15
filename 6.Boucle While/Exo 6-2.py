while True:
    print("\n--- Menu Principal ---")
    print("1 : Dire bonjour")
    print("2 : Additionner deux nombres")
    print("0 : Quitter")
    
    choix = input("Votre choix : ")
    
    if choix == "1":
        print("\nBonjour ! Comment allez-vous ?")
    
    elif choix == "2":
        try:
            nb1 = float(input("Premier nombre : "))
            nb2 = float(input("Deuxième nombre : "))
            print(f"Résultat : {nb1} + {nb2} = {nb1 + nb2}")
        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")
    
    elif choix == "0":
        print("Au revoir !")
        break
    
    else:
        print("Option invalide - veuillez choisir 1, 2 ou 0.")