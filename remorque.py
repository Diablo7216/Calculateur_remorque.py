import streamlit as st
LARGEUR_REMORQUE = 102  # pouces
LONGUEUR_REMORQUE = 53  # pieds
if "palettes" not in st.session_state:
    st.session_state.palettes = []
st.set_page_config(page_title="Calculateur Remorque", layout="centered")
st.title("🚛 Calculateur d'espace remorque")
st.write("Calcul de l'espace plancher utilisé dans une remorque de 53 pieds.")
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
st.subheader("Palettes ajoutées")
for i, p in enumerate(st.session_state.palettes, start=1):
    st.write(
        f"{i}. {p['quantite']} x {p['largeur']:.0f}\" x {p['longueur']:.0f}\""
    )
if st.button("Calculer"):
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
       total_palettes = sum(
        p["quantite"]
        for p in st.session_state.palettes
    )

    st.markdown(
        f"""
        <div style="
            background-color:#d4edda;
            padding:20px;
            border-radius:12px;
            border-left:6px solid #198754;
            margin-top:10px;
        ">
            <h3 style="margin-top:0;">📊 Résumé du chargement</h3>

            <p style="font-size:18px;">
            📦 <b>Nombre de palettes :</b> {total_palettes}
            </p>

            <p style="font-size:18px;">
            📏 <b>Pieds linéaires utilisés :</b> {pieds_lineaires:.2f} pi
            </p>

            <p style="font-size:18px;">
            🚛 <b>Utilisation remorque 53' :</b> {pourcentage:.1f} %
            </p>

            <p style="font-size:18px;">
            ✅ <b>Espace restant :</b> {reste:.2f} pi
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )
`
if st.button("Effacer"):
    st.session_state.palettes = []
    st.rerun()
st.markdown("---")
st.caption("© 2026 Fred Béland")


