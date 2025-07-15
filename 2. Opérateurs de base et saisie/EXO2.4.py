# Demander les trois notes à l'utilisateur
note1 = float(input("Entrez la première note (sur 20) : "))
note2 = float(input("Entrez la deuxième note (sur 20) : "))
note3 = float(input("Entrez la troisième note (sur 20) : "))

# Calculer la moyenne
moyenne = (note1 + note2 + note3) / 3

# Afficher la moyenne et le résultat
print(f"\nMoyenne : {moyenne:.2f}/20")
if moyenne >= 10:
    print("Résultat : Reçu(e) ✅")
else:
    print("Résultat : Non reçu(e) ❌")