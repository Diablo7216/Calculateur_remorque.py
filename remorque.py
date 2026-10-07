import tkinter as tk
from tkinter import ttk, messagebox

LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds

palettes = []


def ajouter_palette():
    try:
        largeur = float(ent_largeur.get())
        longueur = float(ent_longueur.get())
        quantite = int(ent_quantite.get())

        palettes.append({
            "largeur": largeur,
            "longueur": longueur,
            "quantite": quantite
        })

        liste.insert(
            tk.END,
            f"{quantite} x {largeur:.0f}\" x {longueur:.0f}\""
        )

        ent_largeur.delete(0, tk.END)
        ent_longueur.delete(0, tk.END)
        ent_quantite.delete(0, tk.END)

    except:
        messagebox.showerror(
            "Erreur",
            "Vérifiez les dimensions."
        )


def calculer():

    longueur_totale_pouces = 0

    for item in palettes:

        dim1 = item["largeur"]
        dim2 = item["longueur"]
        quantite = item["quantite"]

        # Orientation 1
        palettes_par_rangee_1 = max(
            1,
            int(LARGEUR_REMORQUE // dim1)
        )

        rangees_1 = -(-quantite // palettes_par_rangee_1)
        longueur_1 = rangees_1 * dim2

        # Orientation 2 (palette tournée)
        palettes_par_rangee_2 = max(
            1,
            int(LARGEUR_REMORQUE // dim2)
        )

        rangees_2 = -(-quantite // palettes_par_rangee_2)
        longueur_2 = rangees_2 * dim1

        # Choisir la meilleure orientation
        meilleure_longueur = min(longueur_1, longueur_2)

        longueur_totale_pouces += meilleure_longueur

    pieds_lineaires = longueur_totale_pouces / 12

    pourcentage = (
        pieds_lineaires / LONGUEUR_REMORQUE
    ) * 100

    reste = LONGUEUR_REMORQUE - pieds_lineaires

    resultat.config(
        text=
        f"Pieds linéaires utilisés : {pieds_lineaires:.2f} pi\n\n"
        f"Utilisation remorque 53' : {pourcentage:.1f}%\n\n"
        f"Espace restant : {reste:.2f} pi"
    )

def effacer():
    palettes.clear()
    liste.delete(0, tk.END)
    resultat.config(text="")


# Fenêtre principale

root = tk.Tk()
root.title("Espace Remorque - Fred")
root.geometry("600x550")

titre = tk.Label(
    root,
    text="Calculer l'espace plancher de la remorque",
    font=("Segoe UI", 16, "bold")
)
titre.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Largeur (po)").grid(row=0, column=0, padx=10)
ent_largeur = tk.Entry(frame, width=10)
ent_largeur.grid(row=1, column=0)

tk.Label(frame, text="Longueur (po)").grid(row=0, column=1, padx=10)
ent_longueur = tk.Entry(frame, width=10)
ent_longueur.grid(row=1, column=1)

tk.Label(frame, text="Quantité").grid(row=0, column=2, padx=10)
ent_quantite = tk.Entry(frame, width=10)
ent_quantite.grid(row=1, column=2)

btn_ajouter = ttk.Button(
    root,
    text="Ajouter palette",
    command=ajouter_palette
)
btn_ajouter.pack(pady=10)

liste = tk.Listbox(root, width=50, height=10)
liste.pack(pady=10)

frame_btn = tk.Frame(root)
frame_btn.pack()

ttk.Button(
    frame_btn,
    text="Calculer",
    command=calculer
).grid(row=0, column=0, padx=10)

ttk.Button(
    frame_btn,
    text="Effacer",
    command=effacer
).grid(row=0, column=1, padx=10)

resultat = tk.Label(
    root,
    text="",
    font=("Segoe UI", 12, "bold"),
    justify="left"
)
resultat.pack(pady=20)

signature = tk.Label(
    root,
    text="© 2026 Fred Béland",
    font=("Segoe UI", 8),
    fg="gray"
)

signature.place(
    relx=1.0,
    rely=1.0,
    anchor="se"
)

root.mainloop()