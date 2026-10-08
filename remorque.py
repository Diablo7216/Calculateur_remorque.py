import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Calculateur Remorque",
    layout="centered"
)

# Constantes
LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds

# Initialisation
if "palettes" not in st.session_state:
    st.session_state.palettes = []

# Titre
st.title("🚛 Calculateur d'espace remorque")
st.write("Calcul de l'espace plancher utilisé dans une remorque de 53 pieds.")

# Saisie
col1, col2, col3 = st.columns(3)

with col1:
    largeur = st.number_input(
        "Largeur (po)",
        min_value=1.0,
        value=40.0
    )

with col2:
    longueur = st.number_input(
        "Longueur (po)",
        min_value=1.0,
        value=48.0
    )

with col3:
    quantite = st.number_input(
        "Quantité",
        min_value=1,
        value=1,
        step=1
    )

# Ajouter palette
if st.button("➕ Ajouter palette"):
    st.session_state.palettes.append({
        "largeur": largeur,
        "longueur": longueur,
        "quantite": quantite
    })
    st.rerun()

# Liste des palettes
st.subheader("📦 Palettes ajoutées")

if len(st.session_state.palettes) == 0:
    st.info("Aucune palette ajoutée.")
else:

    for i, p in enumerate(st.session_state.palettes):

        col1, col2 = st.columns([6, 1])

        with col1:
            st.write(
                f"{i+1}. {p['quantite']} x {p['largeur']:.0f} po × {p['longueur''\]:.0f} po"
            )

       
