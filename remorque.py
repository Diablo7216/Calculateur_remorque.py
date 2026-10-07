import streamlit as st

LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds

if "palettes" not in st.session_state:
    st.session_state.palettes = []

st.set_page_config(page_title="Calculateur Remorque", layout="centered")

st.title("🚛 Calculateur d'espace remorque")

st.write(
    "Calcul de l'espace plancher utilisé dans une remorque de 53 pieds."
)

col1, col2, col3 = st.columns(3)

with col1:
    largeur = st.number_input("Largeur (po)", min_value=1.0)

with col2:
    longueur = st.number_input("Longueur (po)", min_value=1.0)

with col3:
    quantite = st.number_input("Quantité", min_value=1, step=1)

if st.button("Ajouter palette"):
    st.session_state.palettes.append({
        "largeur": largeur,
        "longueur": longueur,
        "quantite": quantite
    })

st.
