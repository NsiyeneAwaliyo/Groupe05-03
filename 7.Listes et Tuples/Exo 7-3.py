# Programme d'analyse de liste de nombres
entree = input("Entrez des nombres séparés par des espaces : ")

try:
    # Convertir en liste de nombres flottants
    nombres = [float(x) for x in entree.split()]
    
    if not nombres:
        print("Aucun nombre valide n'a été saisi.")
    else:
        # Calculs
        maximum = max(nombres)
        minimum = min(nombres)
        moyenne = sum(nombres) / len(nombres)
        
        # Affichage des résultats
        print(f"\nRésultats :")
        print(f"Maximum : {maximum}")
        print(f"Minimum : {minimum}")
        print(f"Moyenne : {moyenne:.2f}")  # Arrondi à 2 décimales

except ValueError:
    print("Erreur : veuillez n'entrer que des nombres séparés par des espaces.")1 