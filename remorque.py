import streamlit as st
import pandas as pd

LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds

st.set_page_config(
    page_title="Calculateur Remorque",
    page_icon="🚛",
    layout="wide"
)

# Initialisation
if "palettes" not in st.session_state:
    st.session_state.palettes = []

st.title("🚛 Calculateur d'espace remorque")
st.caption("© 2026 Fred Béland")

st.divider()

# Formulaire
with st.form("ajout_palette", clear_on_submit=True):

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
            value=1
        )

    ajouter = st.form_submit_button(
        "➕ Ajouter palette",
        use_container_width=True
    )

if ajouter:
    st.session_state.palettes.append({
        "Largeur": largeur,
        "Longueur": longueur,
        "Quantité": int(quantite)
    })
    st.success("Palette ajoutée")

# Affichage
if st.session_state.palettes:

    st.subheader("📦 Palettes ajoutées")

    df = pd.DataFrame(st.session_state.palettes)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    total_palettes = sum(
        item["Quantité"]
        for item in st.session_state.palettes
    )

    longueur_totale_pouces = 0

    for item in st.session_state.palettes:

        dim1 = item["Largeur"]
        dim2 = item["Longueur"]
        qty = item["Quantité"]

        palettes_par_rangee_1 = max(
            1,
            int(LARGEUR_REMORQUE // dim1)
        )

        rangees_1 = -(-qty // palettes_par_rangee_1)
        longueur_1 = rangees_1 * dim2

        palettes_par_rangee_2 = max(
            1,
            int(LARGEUR_REMORQUE // dim2)
        )

        rangees_2 = -(-qty // palettes_par_rangee_2)
        longueur
