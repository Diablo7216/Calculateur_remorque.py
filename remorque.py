import streamlit as st
import pandas as pd

LARGEUR_REMORQUE = 102
LONGUEUR_REMORQUE = 53

st.set_page_config(
    page_title="Calculateur Remorque",
    page_icon="🚛",
    layout="wide"
)

if "palettes" not in st.session_state:
    st.session_state.palettes = []

st.title("🚛 Calculateur d'espace remorque")
st.caption("© 2026 Fred Béland")

st.divider()

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

if st.button("➕ Ajouter palette", use_container_width=True):
    st.session_state.palettes.append({
        "Largeur": largeur,
        "Longueur": longueur,
        "Quantité": quantite
    })

if st.session_state.palettes:

    st.subheader("📦 Palettes")

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
        longueur_2 = rangees_2 * dim1

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

    c1.metric(
        "📦 Palettes",
        total_palettes
    )

    c2.metric(
        "📏 Pieds utilisés",
        f"{pieds_lineaires:.1f}"
    )

    c3.metric(
        "🚛 Occupation",
        f"{pourcentage:.1f}%"
    )

    c4.metric(
        "✅ Espace restant",
        f"{reste:.1f} pi"
    )

    st.divider()

    st.subheader("Taux de remplissage")

    st.progress(
        min(int(pourcentage), 100)
    )

    if pourcentage < 80:
        st.success(
            "✅ Espace disponible"
        )

    elif pourcentage < 100:
        st.warning(
            "⚠️ Remorque presque pleine"
        )

    else:
        st.error(
            "❌ Remorque pleine ou dépassée"
        )

    st.subheader("Résumé")

    st.info(
        f"""
        Pieds linéaires utilisés : {pieds_lineaires:.2f} pi

        Utilisation remorque : {pourcentage:.1f} %

        Espace restant : {reste:.2f} pi
        """
    )

colA, colB = st.columns(2)

with colA:
    if st.button(
        "🗑️ Effacer toutes les palettes",
        use_container_width=True
    ):
        st.session_state.palettes = []
        st.rerun()

with colB:
    st.button(
        "🚛 Analyse terminée",
        disabled=True,
        use_container_width=True
    )
