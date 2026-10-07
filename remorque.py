import streamlit as st

LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds

if "palettes" not in st.session_state:
    st.session_state.palettes = []

st.set_page_config(
    page_title="Calculateur Remorque",
    layout="centered"
)

st.title("🚛 Calculateur d'espace remorque")

st.write(
    "Calcul de l'espace plancher utilisé dans une remorque de 53 pieds."
)

# Formulaire avec remise à zéro automatique
with st.form("ajout_palette", clear_on_submit=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        largeur = st.number_input(
            "Largeur (po)",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

    with col2:
        longueur = st.number_input(
            "Longueur (po)",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

    with col3:
        quantite = st.number_input(
            "Quantité",
            min_value=0,
            value=0,
            step=1
        )

    ajouter = st.form_submit_button("➕ Ajouter palette")

if ajouter:

    if largeur > 0 and longueur > 0 and
