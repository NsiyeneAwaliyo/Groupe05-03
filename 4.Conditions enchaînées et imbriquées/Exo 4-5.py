# Programme de sélection de plat
print("Menu du jour - Sélectionnez votre plat")
type_plat = input("Choisissez votre type de plat (viande/poisson/végétarien) : ").lower()

if type_plat == "viande":
    cuisson = input("Comment souhaitez-vous votre viande ? (saignant/à point/bien cuit) : ").lower()
    print(f"Viande {cuisson} commandée !")
    
elif type_plat == "poisson":
    sauce = input("Quelle sauce préférez-vous ? (citron/beurre) : ").lower()
    print(f"Poisson avec sauce {sauce} commandé !")
    
elif type_plat == "végétarien":
    choix = input("Préférez-vous salade ou pâtes ? : ").lower()
    print(f"Plat végétarien ({choix}) commandé !")
    
else:
    print("Type de plat non reconnu - Veuillez choisir entre viande, poisson ou végétarien")