import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------
# Configuração inicial
# ---------------------------------------
st.set_page_config(
    page_title="Calculatrice de l'Empreinte Carbone Scolaire",
    page_icon="🌱",
    layout="wide"
)

st.title("🌍 Calculatrice de l'Empreinte Carbone Scolaire")
st.markdown("""
Cet outil estime **l'empreinte carbone annuelle (t CO₂e/an)** de votre école en tenant compte de :
- Transport institutionnel
- Consommation d'énergie et d'eau
- Production de déchets
- Nombre de personnes (personnel et étudiants)
- Infrastructure physique
- Compensation (plantation d'arbres)

Les calculs sont basés sur des **facteurs d'émission moyens** provenant de sources telles que **IPCC**, **EPA**, **GHG Protocol** et **ANEEL**.
""")

# ---------------------------------------
# Entrées
# ---------------------------------------
st.header("📌 Informations sur l'École")
col1, col2, col3 = st.columns(3)
with col1:
    nome_escola = st.text_input("Nom de l'école", placeholder="Entrez le nom de l'école")
with col2:
    municipio_escola = st.text_input("Commune", placeholder="Entrez la commune")
with col3:
    pais = st.selectbox("Pays", ["Brésil", "France", "Autre"], index=0)

# Transport institutionnel
st.subheader("🚐 Transport Institutionnel")
col1, col2, col3 = st.columns(3)
with col1:
    num_veiculos = st.number_input("Nombre de véhicules", min_value=0, step=1)
with col2:
    num_viagens_mes = st.number_input("Nombre de trajets par mois", min_value=0, step=1)
with col3:
    consumo_combustivel = st.number_input("Consommation mensuelle de carburant (litres)", min_value=0.0, step=0.1)

# Personnes
st.subheader("👩‍🏫 Personnes")
col1, col2 = st.columns(2)
with col1:
    num_funcionarios = st.number_input("Nombre de membres du personnel", min_value=0, step=1)
with col2:
    num_estudantes = st.number_input("Nombre d'étudiants", min_value=0, step=1)

# Infrastructure
st.subheader("🏫 Infrastructure")
col1, col2, col3, col4 = st.columns(4)
with col1:
    num_salas_aula = st.number_input("Salles de classe", min_value=0, step=1)
with col2:
    num_salas_adm = st.number_input("Salles administratives", min_value=0, step=1)
with col3:
    num_laboratorios = st.number_input("Laboratoires", min_value=0, step=1)
with col4:
    num_auditorios = st.number_input("Auditoriums", min_value=0, step=1)

# Énergie
st.subheader("⚡ Énergie")
col1, col2, col3 = st.columns(3)
with col1:
    consumo_energia = st.number_input("Consommation moyenne mensuelle (kWh)", min_value=0.0, step=0.1)
with col2:
    possui_geracao_propria = st.selectbox("Disposez-vous d'une production d'énergie propre ?", ["Non", "Oui"])
with col3:
    geracao_energia = st.text_input("Type et quantité produite mensuellement (kWh)", placeholder="Ex : Solaire, 500 kWh/mois")

# Eau
st.subheader("💧 Eau")
consumo_agua = st.number_input("Consommation moyenne mensuelle d'eau (litres)", min_value=0.0, step=10.0)

# Déchets
st.subheader("🗑️ Production de Déchets")
volume_lixo = st.number_input("Volume de déchets générés par mois (kg)", min_value=0.0, step=1.0)

# Compensation
st.subheader("🌳 Mesures de Compensation")
arvores = st.number_input("Arbres plantés", min_value=0, step=1)

st.markdown("---")

# ---------------------------------------
# Calculs
# ---------------------------------------
if st.button("Calculer l'Empreinte Carbone"):
    # --- Facteurs d'émission approximatifs ---
    fator_combustivel = 2.31  # kg CO2e/litre (essence/diesel moyenne) - IPCC
    fator_energia = 0.084     # kg CO2e/kWh (Brésil, matrice propre - ANEEL 2023)
    fator_agua = 0.0003       # kg CO2e/litre (traitement et pompage)
    fator_lixo = 1.9          # kg CO2e/kg de déchets non recyclés
    fator_arvore = 22         # kg CO2e capturé/arbre/an (moyenne conservatrice - FAO)
    
    # Personnes : moyenne de 0,5 t CO2e/personne/an en contexte scolaire
    fator_pessoa = 500  # kg CO2e par personne/an
    
    # Infrastructure : estimation par type d'espace
    fator_sala_aula = 150    # kg CO2e/an par salle de classe
    fator_sala_adm = 100
    fator_lab = 300
    fator_auditorio = 500

    # --- Calcul par secteur ---
    # Transport
    emissao_transporte = consumo_combustivel * fator_combustivel * 12

    # Énergie
    emissao_energia = consumo_energia * fator_energia * 12

    # Eau
    emissao_agua = consumo_agua * fator_agua * 12

    # Déchets
    emissao_lixo = volume_lixo * fator_lixo * 12

    # Personnes
    total_pessoas = num_funcionarios + num_estudantes
    emissao_pessoas = total_pessoas * fator_pessoa

    # Infrastructure
    emissao_infra = (
        num_salas_aula * fator_sala_aula +
        num_salas_adm * fator_sala_adm +
        num_laboratorios * fator_lab +
        num_auditorios * fator_auditorio
    )

    # --- Total et compensation ---
    emissao_total_kg = (emissao_transporte + emissao_energia + emissao_agua +
                        emissao_lixo + emissao_pessoas + emissao_infra)

    emissao_total_t = emissao_total_kg / 1000  # tonnes

    compensacao_kg = arvores * fator_arvore
    emissao_liquida_t = (emissao_total_kg - compensacao_kg) / 1000

    # ---------------------------------------
    # Résultats
    # ---------------------------------------
    st.success(f"🌱 **Empreinte carbone estimée (totale) : {emissao_total_t:.2f} t CO₂e/an**")
    st.info(f"Après compensation par les arbres : **{emissao_liquida_t:.2f} t CO₂e/an**")

    # ---------------------------------------
    # Graphiques
    # ---------------------------------------
    data = {
        "Secteur": [
            "Transport", "Énergie", "Eau", "Déchets",
            "Personnes (personnel + étudiants)",
            "Infrastructure"
        ],
        "Émissions (kg CO₂e/an)": [
            emissao_transporte, emissao_energia, emissao_agua,
            emissao_lixo, emissao_pessoas, emissao_infra
        ]
    }
    df = pd.DataFrame(data)

    col1, col2 = st.columns([2, 1])

    with col1:
        fig = px.pie(
            df,
            values="Émissions (kg CO₂e/an)",
            names="Secteur",
            title="Répartition des Émissions par Secteur",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Résumé Numérique")
        st.dataframe(df.style.format({"Émissions (kg CO₂e/an)": "{:.2f}"}))

    # ---------------------------------------
    # Rapport détaillé
    # ---------------------------------------
    st.markdown("---")
    st.subheader("📊 Rapport Détaillé")

    st.markdown(f"""
    ### Résumé général
    - **Nom de l'école :** {nome_escola}
    - **Commune :** {municipio_escola}
    - **Pays :** {pais}
    - **Total de personnes :** {total_pessoas} (Personnel : {num_funcionarios}, Étudiants : {num_estudantes})
    - **Émissions totales (sans compensation) :** {emissao_total_t:.2f} t CO₂e/an
    - **Compensation par les arbres :** {compensacao_kg/1000:.2f} t CO₂e/an
    - **Émissions nettes :** {emissao_liquida_t:.2f} t CO₂e/an
    """)

    st.markdown("### Détails par secteur")
    st.markdown("""
    - **Transport :** Calcul basé sur la consommation de carburant fournie.  
    - **Énergie :** Prend en compte la matrice électrique brésilienne (0,084 kg CO₂e/kWh).  
    - **Eau :** Émissions dues au captage, traitement et pompage.  
    - **Déchets :** Considère les déchets communs non recyclés.  
    - **Personnes :** Estimation de 0,5 t CO₂e/personne/an incluant alimentation, déplacements et activités indirectes.  
    - **Infrastructure :** Basé sur la maintenance, la climatisation, le nettoyage et la consommation fixe par type d'espace.  
    """)

    st.markdown("### Formules utilisées")
    st.markdown("""
    - **Transport :** Consommation mensuelle (L) × 2,31 × 12  
    - **Énergie :** Consommation mensuelle (kWh) × 0,084 × 12  
    - **Eau :** Consommation mensuelle (L) × 0,0003 × 12  
    - **Déchets :** Volume mensuel (kg) × 1,9 × 12  
    - **Personnes :** Total de personnes × 500 kg CO₂e/an  
    - **Infrastructure :**
      - Salle de classe : 150 kg/an  
      - Salle administrative : 100 kg/an  
      - Laboratoire : 300 kg/an  
      - Auditorium : 500 kg/an  
    - **Compensation par arbres :** 22 kg CO₂e/an par arbre
    """)

    st.write("---")
    st.markdown("### Limitations et Avertissements")
    st.caption("⚠️ Cette calculatrice est un prototype éducatif avec des estimations simplifiées. Pour des inventaires officiels, suivez le GHG Protocol, ISO 14064/14067 et d'autres références internationales.")
