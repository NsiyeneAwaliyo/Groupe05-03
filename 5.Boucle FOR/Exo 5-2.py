# Variante avec affichage détaillé
entree = input("Entrez des nombres entiers séparés par des espaces : ")

nombres = []
for x in entree.split():
    try:
        nombres.append(int(x))
    except ValueError:
        print(f"Attention : '{x}' n'est pas un nombre entier et sera ignoré")

nombres_pairs = [x for x in nombres if x % 2 == 0]
        
print("\nNombres pairs trouvés :", nombres_pairs)
print("La somme des nombres pairs est :", sum(nombres_pairs))