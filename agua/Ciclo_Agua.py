import streamlit as st

st.set_page_config(page_title="Fórum França-Brasil", page_icon=":earth_americas:", layout="wide")


col_fr_title, col_br_title = st.columns(2)
with col_fr_title:
    st.title("💧 Cycle de l'eau")
    
with col_br_title:
    st.title("💧 Ciclo da Água")

col_fr, col_br = st.columns([1, 1])

with col_fr:
    st.info(":droplet: Dynamique du Cycle de l'Eau dans les Forêts Tempérées")
    st.markdown("""
    ### :bulb: **Éléments du Cycle de l'Eau**
    - **Précipitations** : Modérées à fortes, avec des variations saisonnières.
    - **Interception par la Végétation** : La végétation intercepte une partie des précipitations.
    - **Évapotranspiration** : Modérée en raison des variations saisonnières de température.
    - **Infiltration et Percolation** : L'eau s'infiltre dans le sol en fonction de sa composition et de la profondeur des racines.
    - **Écoulement Superficiel et Subsuperficiel** : Influencé par la topographie et la densité de la végétation.

    ### :clipboard: **Facteurs Climatiques et Environnementaux**
    - **Température** : Affecte le taux d'évaporation et de transpiration.
    - **Couverture Végétale** : Influence l'interception de l'eau de pluie et l'évapotranspiration.
    - **Type de Sol et Capacité de Rétention d'Eau** : Les sols varient dans leur capacité à retenir l'eau.

    ### :warning: **Impacts Anthropiques**
    - Le déboisement et la dégradation des sols réduisent l'infiltration et augmentent l'écoulement.
    - Les changements climatiques peuvent modifier les précipitations et perturber l'équilibre du cycle de l'eau.
    """)

    st.markdown("""
    ### :seedling: **Méthodes d'Étude**
    - Mesures directes des précipitations, de l'écoulement et de l'évapotranspiration.
    - Utilisation de capteurs et de modèles hydrologiques pour prévoir la dynamique du cycle de l'eau.
    - Suivi des changements dans le temps pour observer les impacts des variations climatiques et de l'utilisation des sols.
    
    ### :evergreen_tree: **Impacts sur l'Écosystème**
    - **Biodiversité** : La dynamique de l'eau est essentielle pour la biodiversité, en particulier dans les forêts tropicales.
    - **Services Écosystémiques** : Les forêts contribuent à la régulation du climat, au maintien des bassins hydrographiques et à l'approvisionnement en eau des populations locales.
    """)

with col_br:
    st.info(":droplet: Dinâmica do Ciclo da Água em Florestas Temperadas")
    st.markdown("""
    ### :bulb: **Componentes do Ciclo da Água**
    - **Precipitação**: Moderada a alta, com variações sazonais.
    - **Intercepção pela Vegetação**: Vegetação intercepta parte da precipitação.
    - **Evapotranspiração**: Moderada devido às variações de temperatura sazonais.
    - **Infiltração e Percolação**: A quantidade infiltrada no solo depende do tipo de solo e profundidade das raízes.
    - **Escoamento Superficial e Subsuperficial**: Influenciado pela topografia e densidade da vegetação.

    ### :clipboard: **Fatores Climáticos e Ambientais**
    - **Temperatura**: Influencia a taxa de evaporação e transpiração.
    - **Cobertura Vegetal**: A vegetação impacta a interceptação de chuva e evapotranspiração.
    - **Tipo de Solo e Capacidade de Retenção de Água**: Solos variam em sua capacidade de retenção de água.

    ### :warning: **Impactos Antropogênicos**
    - O desmatamento e a degradação do solo impactam negativamente a infiltração e o escoamento.
    - Mudanças climáticas podem alterar a precipitação e o equilíbrio do ciclo da água.
    """)

    st.markdown("""
    ### :seedling: **Métodos de Estudo**
    - Medições diretas de precipitação, escoamento e evapotranspiração.
    - Uso de sensores e modelos hidrológicos para prever a dinâmica do ciclo da água.
    - Monitoramento de mudanças ao longo do tempo para observar o impacto das variações climáticas e de uso do solo.
    
    ### :evergreen_tree: **Impactos no Ecossistema**
    - **Biodiversidade**: A dinâmica da água é essencial para a biodiversidade, especialmente em florestas tropicais.
    - **Serviços Ecossistêmicos**: As florestas contribuem para a regulação do clima, manutenção de bacias hidrográficas e fornecimento de água para populações locais.
    """)


