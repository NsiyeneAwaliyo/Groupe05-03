def renverser_liste(liste):
    liste_renversee = []
    index = len(liste) - 1  # Commence par le dernier élément
    
    while index >= 0:
        liste_renversee.append(liste[index])
        index -= 1  # Décrémente pour parcourir à l'envers
    
    return liste_renversee

# Demander la liste à l'utilisateur
elements = input("Entrez des éléments séparés par des espaces : ").split()

# Appliquer la fonction
resultat = renverser_liste(elements)
print("Liste renversée :", resultat)