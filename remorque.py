import streamlit as st
import pandas as pd
from io import BytesIO

LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds

st.set_page_config(
    page_title="Calculateur Remorque",
    layout="centered"
)

if "palettes" not in st.session_state:
    st.session_state.palettes = []

st.title("🚛 Calculateur d'espace remorque")
st.write("Calcul de l'espace plancher utilisé dans une remorque de 53 pieds.")

# SAISIE
col1, col2, col3 = st.columns(3)

with col1:
    largeur = st.number_input("Largeur (po)", min_value=1)

with col2:
    longueur = st.number_input("Longueur (po)", min_value=1)

with col3:
    quantite = st.number_input("Quantité", min_value=1, step=1)

if st.button("➕ Ajouter palette"):
    st.session_state.palettes.append({
        "largeur": largeur,
        "longueur": longueur,
        "quantite": quantite
    })

# LISTE DES PALETTES
st.subheader("📦 Palettes ajoutées")

for i, p in enumerate(st.session_state.palettes):

    col1, col2 = st.columns([8, 1])

    with col1:
        st.write(
            f"{i+1}. {p['quantite']} x {int(p['largeur'])}\" x {int(p['longueur'])}\""
        )

    with col2:
        if st.button("🗑️", key=f"delete_{i}"):
            st.session_state.palettes.pop(i)
            st.rerun()

# CALCUL
if st.button("📊 Calculer"):

    longueur_totale_pouces = 0

    for item in st.session_state.palettes:

        dim1 = item["largeur"]
  
