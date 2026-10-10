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
    reste = LONGUEUR_REMORQUE - pieds_lineaires

    if pourcentage > 90:
        st.error("🔴 Remorque presque pleine")
    elif pourcentage > 75:
        st.warning("🟡 Attention : espace limité")
    else:
        st.info("🟢 Espace disponible")

    st.progress(min(int(pourcentage), 100))

    st.caption(
        f"Remplissage de la remorque : {pourcentage:.1f}%"
    )

    total_palettes = sum(
        p["quantite"]
        for p in st.session_state.palettes
    )

    st.success(
        f"""
&nbsp;📦 Nombre de palettes : {total_palettes}

📏 Pieds linéaires utilisés : {pieds_lineaires:.2f} pi

🚛 Utilisation remorque 53' : {pourcentage:.1f} %

✅ Espace restant : {reste:.2f} pi
"""
    )

if st.button("🗑️ Effacer"):
    st.session_state.palettes = []
    st.rerun()

st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; color:#7f8c8d; font-size:12px;'>
        🚛 Calculateur de chargement remorque 53' <br>
        © 2026 Fred Béland | Version 1.0
    </div>
    """,
    unsafe_allow_html=True
)

  
