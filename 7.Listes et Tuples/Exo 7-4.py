# Liste des étudiants avec leurs notes
etudiants = [
    ("Alice", 18),
    ("Bob", 12),
    ("Clara", 15),
    ("David", 20),
    ("Emma", 14),
    ("Félix", 16)
]

# Afficher les étudiants avec note >= 15
print("Étudiants avec une note ≥ 15 :")
for nom, note in etudiants:
    if note >= 15:
        print(f"- {nom} : {note}/20")
