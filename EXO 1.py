# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 12:35:34 2025

@author: congo
"""

# Demander les informations à l'utilisateur
print("Créez votre mini profil\n" + "="*30)
prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

# Calculer l'âge en jours (approximation)
age_en_jours = age * 365

# Afficher le profil structuré
print("\nMini Profil")
print("-"*30)
print(f"Prénom: {prenom}")
print(f"Âge: {age} ans (soit environ {age_en_jours} jours)")
print(f"Ville: {ville}")
print(f"Métier: {metier}")
print("-"*30)
print("Merci d'avoir créé votre profil!")