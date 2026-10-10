import streamlit as st
# Configuration
st.set_page_config(
    page_title="Calculateur Remorque",
    page_icon="🚛",
    layout="centered"
)
# Style CSS
st.markdown("""
<style>
div[data-testid="metric-container"] {
    background: white;
    border: 1px solid #e5e7eb;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}
.stProgress > div > div > div > div {
    height: 22px;
    border-radius: 10px;
}
h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
# Constantes
LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds
# Session
if "palettes" not in st.session_state:
    st.session_state.palettes = []
# En-tête
st.markdown(
    "<h1>🚛 Calculateur de chargement remorque</h1>",
    unsafe_allow_html=True
)
st.caption(
    "Optimisation du chargement d'une remorque de 53 pieds"
)
# Saisie
col1, col2, col3 = st.columns(3)
with col1:
    largeur = st.number_input(
        "Largeur (po)",
        min_value=1,
        value=48
    )
with col2:
    longueur = st.number_input(
        "Longueur (po)",
        min_value=1,
        value=40
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
    st.session_state.palettes.append(
        {
            "largeur": largeur,
            "longueur": longueur,
            "quantite": quantite
        }
    )
    st.rerun()
# Liste des palettes
st.subheader("📦 Palettes ajoutées")
for i, p in enumerate(st.session_state.palettes):
    c1, c2 = st.columns([8, 1])
    with c1:
        st.write(
            f"{i+1}. {p['quantite']} x {int(p['largeur'])}\" x {int(p['longueur'])}\""
        )
    with c2:
        if st.button("🗑️", key=f"supprimer_{i}"):
            st.session_state.palettes.pop(i)
            st.rerun()
# Calcul
if st.button("📊 Calculer"):
    longueur_totale_pouces = 0
    for item in st.session_state.palettes:
        dim1 = item["largeur"]
        dim2 = item["longueur"]
        qty = item["quantite"]
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
        pieds_lineaires /
        LONGUEUR_REMORQUE
    ) * 100
    reste = LONGUEUR_REMORQUE - pieds_lineaires
    total_palettes = sum(
        p["quantite"]
        for p in st.session_state.palettes
    )
    st.markdown("### 📊 Tableau de bord")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "📦 Palettes",
            total_palettes
        )
    with col2:
        st.metric(
            "📏 Utilisé",
            f"{pieds_lineaires:.1f} pi"
        )
    with col3:
        st.metric(
            "✅ Restant",
            f"{reste:.1f} pi"
        )
    with col4:
        st.metric(
            "🚛 Occupation",
            f"{pourcentage:.1f}%"
        )
    

