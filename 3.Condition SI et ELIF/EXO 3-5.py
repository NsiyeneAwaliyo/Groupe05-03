# Programme de vérification de mot de passe
mot_de_passe = input("Créez votre mot de passe : ")

# Initialisation des vérifications
longueur_ok = len(mot_de_passe) >= 8
contient_chiffre = any(caractere.isdigit() for caractere in mot_de_passe)
contient_majuscule = any(caractere.isupper() for caractere in mot_de_passe)

# Vérification globale
if longueur_ok and contient_chiffre and contient_majuscule:
    print("Mot de passe valide ✅")
else:
    print("Mot de passe invalide ❌")
    
    # Messages d'erreur détaillés
    if not longueur_ok:
        print("- Doit contenir au moins 8 caractères")
    if not contient_chiffre:
        print("- Doit contenir au moins un chiffre")
    if not contient_majuscule:
        print("- Doit contenir au moins une majuscule")