import streamlit as st
import pandas as pd

LARGEUR_REMORQUE = 102
LONGUEUR_REMORQUE = 53

st.set_page_config(
    page_title="Calculateur Remorque",
    page_icon="🚛",
    layout="wide"
)

# Initialisation
if "palettes" not in st.session_state:
    st.session_state.palettes = []

if "largeur" not in st.session_state:
    st.session_state.largeur = 40.0

if "longueur" not in st.session_state:
    st.session_state.longueur = 48.0

if "quantite" not in st.session_state:
    st.session_state.quantite = 1

# Titre
st.title("🚛 Calculateur d'espace remorque")
st.caption("© 2026 Fred Béland")

st.divider()

# Saisie
col1, col2, col3 = st.columns(3)

with col1:
    largeur = st.number_input(
        "Largeur (po)",
        min_value=1.0,
        key="largeur"
    )

with col2:
    longueur = st.number_input(
        "Longueur (po)",
        min_value=1.0,
        key="longueur"
    )

with col3:
    quantite = st.number_input(
        "Quantité",
        min_value=1,
        key="quantite"
    )

# Ajouter palette
if st.button("➕ Ajouter palette", use_container_width=True):

    st.session_state.palettes.append({
        "Largeur": largeur,
        "Longueur": longueur,
        "Quantité": quantite
    })

    # Remise des champs aux valeurs par défaut
    st.session_state.largeur = 40.0
    st.session_state.longueur = 48.0
    st.session_state.quantite = 1

    st.rerun()

# Tableau
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

        largeur_palette = item["Largeur"]
        longueur_palette = item["Longueur"]
        quantite_palette = item["Quantité"]

        palettes_par_rangee_1 = max(
            1,
            int(LARGEUR_REMORQUE // largeur_palette)
        )

        rangees_1 = -(-quantite_palette // palettes_par_rangee_1)
        longueur_1 = rangees_1 * longueur_palette

        palettes_par_rangee_2 = max(
            1,
            int(LARGEUR_REMORQUE // longueur_palette)
        )

        rangees_2 = -(-quantite_palette // palettes_par_rangee_2)
        longueur_2 = rangees_2 * largeur_palette

        meilleure_longueur = min(
            longueur_1,
            longueur_2
        )

        longueur_totale_pouces += meilleure_longueur

    pieds_lineaires = longueur_totale_pouces / 12

    pourcentage = (
        pieds_lineaires / LONGUEUR_REMORQUE
    ) * 100

    reste = LONGUEUR_REMORQUE - pieds_lineaires

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📦 Total palettes",
            total_palettes
        )

    with c2:
        st.metric(
            "📏 Pieds utilisés",
            f"{pieds_lineaires:.2f}"
        )

    with c3:
        st.metric(
            "🚛 Occupation",
            f"{pourcentage:.1f}%"
        )

    with c4:
        st.metric(
            "✅ Restant",
            f"{reste:.2f} pi"
        )

    st.divider()

    st.subheader("Taux de remplissage")

    st.progress(
        min(int(pourcentage), 100)
    )

    if pourcentage < 80:
        st.success("✅ Espace disponible")

    elif pourcentage < 100:
        st.warning("⚠️ Remorque presque pleine")

    else:
        st.error("❌ Remorque pleine ou dépassée")

    st.subheader("Résumé")

    st.
