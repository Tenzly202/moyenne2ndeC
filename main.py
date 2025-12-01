# Calcul de la moyenne pondérée (division finale par 23)
# Matières et coefficients donnés :
# Français x3, Maths x5, Pc x4, Svt x2, Esp x1, AnG x3, HG x2, Mus x1, ESP x1
# (Remarque : "Esp" et "ESP" sont gardés séparés comme dans ta liste.)

def demander_note(matiere):
    while True:
        try:
            n = input(f"Note en {matiere} (0-20) : ").strip().replace(',', '.')
            note = float(n)
            if 0 <= note <= 20:
                return note
            else:
                print("Entrer une note entre 0 et 20.")
        except ValueError:
            print("Valeur non reconnue : entrez un nombre (ex. 12.5).")

def calcul_moyenne_div23():
    # dictionnaire matière:coefficient
    coeffs = {
        "FR": 3,
        "MATHS": 5,
        "PC": 4,
        "SVT": 2,
        "ESP": 1,
        "ANG": 3,
        "HG": 2,
        "MUS": 1,
        "EPS": 1 

    }

    # récupérer les notes
    notes = {}
    for matiere in coeffs:
        notes[matiere] = demander_note(matiere)

    # calcul de la somme pondérée
    somme_ponderee = sum(notes[m] * coeffs[m] for m in coeffs)

    # division finale par 23 (selon ta consigne)
    moyenne = somme_ponderee / 23

    print("\n--- Résultat ---")
    for m in coeffs:
        print(f"{m} : note={notes[m]:.2f} × coeff={coeffs[m]}")
    print(f"\nSomme pondérée = {somme_ponderee:.2f}")
    print(f"Moyenne (somme pondérée / 23) = {moyenne:.2f}")

if __name__ == "__main__":
    calcul_moyenne_div23()