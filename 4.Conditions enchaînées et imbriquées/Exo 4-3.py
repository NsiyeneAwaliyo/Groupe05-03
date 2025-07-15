# Programme d'évaluation de santé
print("Questionnaire de santé simplifié")

fievre = input("Avez-vous de la fièvre ? (oui/non) : ").lower()

if fievre == "oui":
    douleurs = input("Avez-vous des douleurs ? (oui/non) : ").lower()
    print("Consulter un médecin")
elif fievre == "non":
    toux = input("Avez-vous une toux ? (oui/non) : ").lower()
    if toux == "oui":
        print("Repos conseillé")
    else:
        print("Bonne santé")
else:
    print("Réponse non reconnue - Veuillez répondre par 'oui' ou 'non'")