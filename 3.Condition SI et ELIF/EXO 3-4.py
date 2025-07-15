# Programme de conseil météorologique
temperature = float(input("Entrez la température actuelle (en °C) : "))

if temperature >= 35:
    conseil = "Très chaud, restez hydraté."
elif 25 <= temperature <= 34:
    conseil = "Chaud, faites attention au soleil."
elif 15 <= temperature <= 24:
    conseil = "Température agréable."
else:
    conseil = "Il fait frais, couvrez-vous."

print(f"\nÀ {temperature:.1f}°C : {conseil}")