# Programme de contrôle d'accès
print("Système de contrôle d'accès")
role = input("Entrez votre rôle (employé/visiteur/sécurité) : ").lower()

if role == "employé":
    badge = input("Avez-vous un badge valide ? (oui/non) : ").lower()
    if badge == "oui":
        print("Accès autorisé pour l'employé")
    else:
        print("Accès refusé : badge invalide")

elif role == "visiteur":
    rdv = input("Avez-vous un rendez-vous ? (oui/non) : ").lower()
    if rdv == "oui":
        print("Accès autorisé pour le visiteur")
    else:
        print("Accès refusé : rendez-vous nécessaire")

elif role == "sécurité":
    print("Accès autorisé pour l'agent de sécurité")

else:
    print("Rôle non reconnu - Accès refusé")