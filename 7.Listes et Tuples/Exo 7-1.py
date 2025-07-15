# Fonction de tri à bulles
def tri_a_bulles(liste):
    n = len(liste)
    # Parcourir tous les éléments
    for i in range(n):
        # Les i derniers éléments sont déjà en place
        for j in range(0, n-i-1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

# Demander la liste de nombres
entree = input("Entrez des nombres séparés par des espaces : ")

try:
    # Convertir en liste de nombres
    nombres = [float(x) for x in entree.split()]
    
    if not nombres:
        print("Aucun nombre entré.")
    else:
        # Appliquer le tri à bulles
        tri_a_bulles(nombres)
        
        # Afficher le résultat
        print("Liste triée :", nombres)

except ValueError:
    print("Erreur : veuillez n'entrer que des nombres séparés par des espaces.")