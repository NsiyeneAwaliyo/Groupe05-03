import random

# Générer un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)
essais = 0

print("Devinez le nombre secret entre 1 et 100 !")

while True:
    try:
        # Demander la proposition du joueur
        proposition = int(input("Votre proposition : "))
        essais += 1
        
        # Vérifier la proposition
        if proposition < nombre_secret:
            print("Trop petit !")
        elif proposition > nombre_secret:
            print("Trop grand !")
        else:
            print(f"Bravo ! Vous avez trouvé en {essais} essais.")
            break
            
    except ValueError:
        print("Veuillez entrer un nombre valide entre 1 et 100.")