with st.form("ajout_palette", clear_on_submit=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        largeur = st.number_input(
            "Largeur (po)",
            min_value=1.0,
            value=0.0
        )

    with col2:
        longueur = st.number_input(
            "Longueur (po)",
            min_value=1.0,
            value=0.0
        )

    with col3:
        quantite = st.number_input(
            "Quantité",
            min_value=1,
            value=1
        )

    ajouter = st.form_submit_button("Ajouter palette")

if ajouter:
    st.session_state.palettes.append({
        "largeur": largeur,
        "longueur": longueur,
        "quantite": quantite
    })
