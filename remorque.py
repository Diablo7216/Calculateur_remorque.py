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

    st.markdown(f"""
    <div style="
        background-color:#d4edda;
        padding:20px;
        border-radius:10px;
        border-left:6px solid #28a745;
        font-size:18px;
    ">
        <b>📦 Nombre de palettes :</b> {total_palettes}<br><br>
        <b>📏 Pieds linéaires utilisés :</b> {pieds_lineaires:.2f} pi<br><br>
        <b>🚛 Utilisation remorque 53' :</b> {pourcentage:.1f}%<br><br>
        <b>✅ Espace restant :</b> {reste:.2f} pi
    </div>
    """, unsafe_allow_html=True)
