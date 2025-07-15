# Liste de livres (chaque livre est un dictionnaire)
bibliotheque = [
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "année": 1943},
    {"titre": "1984", "auteur": "George Orwell", "année": 1949},
    {"titre": "Dune", "auteur": "Frank Herbert", "année": 1965},
    {"titre": "Le Probleme à trois corps", "auteur": "Liu Cixin", "année": 2008},
    {"titre": "Sapiens", "auteur": "Yuval Noah Harari", "année": 2011},
    {"titre": "The Martian", "auteur": "Andy Weir", "année": 2014},
    {"titre": "Guerre et Paix", "auteur": "Léon Tolstoï", "année": 1869}
]

# Afficher les livres publiés après 2010
print("Livres publiés après 2010 :")
for livre in bibliotheque:
    if livre["année"] > 2010:
        print(f"- {livre['titre']} par {livre['auteur']} ({livre['année']})")