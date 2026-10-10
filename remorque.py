import streamlit as st

LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds

if "palettes" not in st.session_state:
    st.session_state.palettes = []

st.set_page_config(
    page_title="Calculateur Remorque",
    layout="centered"
)
st.markdown("""
<style>

div[data-testid="metric-container"]{
    background:#ffffff;
    border:1px solid #e5e7eb;
    padding:18px;
    border-radius:15px;
    box-shadow:0 4px 10px rgba(0,0,0,.08);
}

.stProgress > div > div > div > div{
    height:28px;
    border-radius:15px;
}

h1{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.title("🚛 Calculateur d'espace remorque")
st.write("Calcul de l'espace plancher utilisé dans une remorque de 53 pieds.")

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
    pourcentage = (pieds_lineaires / LONGUEUR_REMORQUE) * 100
    reste = max(0, LONGUEUR_REMORQUE - pieds_lineaires)
    debordement = max(0, pieds_lineaires - LONGUEUR_REMORQUE)
    total_palettes = sum(
        p["quantite"]
        for p in st.session_state.palettes
    )

    # Tableau de bord
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📦 Palettes", total_palettes)

    with col2:
        st.metric("📏 Utilisé", f"{pieds_lineaires:.1f} pi")

    with col3:
    if pourcentage > 100:
        st.metric(
            "🚨 Débordement",
            f"{debordement:.1f} pi"
        )
    else:
        st.metric(
            "✅ Restant",
            f"{reste:.1f} pi"
        )

    with col4:
        st.metric("🚛 Occupation", f"{pourcentage:.1f}%")

    # Messages d'état
    if pourcentage > 100:
        st.error(
            f"🚨 Débordement de {pourcentage - 100:.1f}% - Une seule remorque ne suffit pas !"
        )
    elif pourcentage > 90:
        st.error("🔴 Remorque presque pleine")
    elif pourcentage > 75:
        st.warning("🟡 Attention : espace limité")
    else:
        st.success("🟢 Espace disponible")

    # Barre de progression
    st.progress(min(pourcentage / 100, 1.0))

    st.markdown(
        f"""
        <div style='text-align:center; font-weight:bold;'>
            Remplissage de la remorque : {pourcentage:.1f}%
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("🗑️ Effacer"):
    st.session_state.palettes = []
    st.rerun()

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:#7f8c8d; font-size:12px;'>
        🚛 Calculateur de chargement remorque 53'<br>
        © 2026 Fred Béland | Version 1.0
    </div>
    """,
    unsafe_allow_html=True
)

