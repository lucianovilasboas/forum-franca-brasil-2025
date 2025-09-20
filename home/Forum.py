import streamlit as st

# Configuração da página
st.set_page_config(page_title="Fórum Ciência e Sociedade 2025", page_icon=":earth_americas:", layout="wide")

# Título principal
col_fr_title, col_br_title = st.columns(2)
with col_fr_title:
    st.title(":earth_africa: Forum Science et Société 2025")

with col_br_title:
    st.title(":earth_americas: Fórum Ciência e Sociedade 2025")

# Criação das duas colunas
col_fr, col_br = st.columns([1, 1])

# ==============================
# COLUNA EM FRANCÊS
# ==============================
with col_fr:
    st.info(":blue_heart: Version française")

    st.markdown("""
    ### 🌍 **Forum franco-brésilien Science et Société**
    Le **Forum franco-brésilien Science et Société** est une initiative internationale qui, depuis 2005, 
    favorise le dialogue entre étudiants, professeurs, chercheurs et autorités du Brésil et de la France 
    sur des sujets d'importance scientifique et sociale.  

    L'événement a lieu alternativement dans les deux pays et vise à **stimuler les échanges culturels, académiques et scientifiques**.

    L'année **2025** sera particulièrement symbolique, car elle marquera :
    - La **8ème édition** du Forum,  
    - **20 ans** de sa création,  
    - Et les **200 ans de relations diplomatiques** entre le Brésil et la France, durant l'*Année du Brésil en France et Année de la France au Brésil*.
    """)

    st.subheader("🎯 Thème et Sous-thèmes")
    st.markdown("""
    **Thème central :**  
    *Systèmes alimentaires et changements climatiques : défis et perspectives*

    Ce choix reflète les défis mondiaux auxquels sont confrontés les deux pays, notamment dans les domaines de la production agricole et de la durabilité environnementale.

    **Sous-thèmes :**
    - 🌱 **Technologies et stratégies pour une production agricole durable :**  
      Solutions techniques et méthodologiques pour améliorer la production sans compromettre l'environnement.
    - 💧 **Gestion des ressources naturelles :**  
      Stratégies pour l'utilisation rationnelle et durable de ressources telles que l'eau, le sol et les engrais organiques.
    - 🤝 **Rôle individuel et collectif dans la lutte contre les changements climatiques :**  
      Le rôle de la société, des communautés et des institutions dans la construction de solutions à la crise climatique.
    """)

    st.subheader("🏛️ Organisation et Institutions impliquées")
    st.markdown("""
    L'**organisation** de l'édition 2025 est assurée par l'**Institut Fédéral d'Éducation, de Science et de Technologie de Minas Gerais (IFMG)**, au Brésil, avec le soutien de partenaires nationaux et internationaux :

    - CONIF – Conseil National des Institutions du Réseau Fédéral (Brésil)
    - SETEC/MEC – Secrétariat de l'Éducation Professionnelle et Technologique (Brésil)
    - Ministère de l'Agriculture et de la Souveraineté Alimentaire (France, DGER)
    - Réseau Brésil de l’Enseignement Agricole
    - Ambassade de France au Brésil
    - Embrapa – Entreprise Brésilienne de Recherche Agricole
    - Ministère du Développement Agraire et de l'Agriculture Familiale (Brésil)
    - Ministère de l'Agriculture et de l'Élevage (Brésil)

    La **Commission d'organisation** comprend des représentants des campus IFMG Bambuí, Ouro Preto et Santa Luzia,
    ainsi que des membres d'autres Instituts Fédéraux et des volontaires.
    """)

    st.subheader("📍 Lieu de l'événement")
    st.markdown("""
    La 8ème édition se déroulera au **Campus IFMG Bambuí**, situé à environ 270 km de Belo Horizonte.

    Bambuí est une ville du Minas Gerais comptant environ **25 000 habitants**, avec une économie tournée vers l'agriculture et l'élevage.  
    Le Campus couvre **328,76 hectares** et dispose d'une infrastructure moderne, avec des laboratoires, des auditoriums,
    des zones expérimentales et des espaces culturels, offrant des cours techniques, de premier cycle et de troisième cycle.

    **Adresse :** Fazenda Varginha, Rodovia Bambuí/Medeiros - km 05, Caixa Postal 05, Bambuí - MG, CEP : 38.900-000.
    """)

    st.subheader("🗓️ Calendrier du Forum")
    st.markdown("""
    - **Phase de sensibilisation :** jusqu'au 11/10/2025  
      Développement de projets communs entre institutions brésiliennes et françaises.

    - **Pré-forum :** 12 au 18/10/2025  
      Visite des délégations françaises dans leurs institutions partenaires au Brésil.

    - **Déplacement vers Bambuí :** 19/10/2025  
      Transport organisé par la commission, avec accueil à l'aéroport de Confins.

    - **Forum à l'IFMG Bambuí :** 20 au 24/10/2025  
      Ateliers techniques et artistiques, conférences, débats, présentations culturelles et visites techniques.

    - **Retour des délégations :** 25/10/2025  
      Vols programmés pour l'après-midi, à partir de 15h.
    """)

    st.subheader("👥 Public cible")
    st.markdown("""
    L'événement réunira environ **250 participants**, dont :
    - Professeurs/formateurs et étudiants (1 professeur + 4 étudiants par institution) ;
    - Chercheurs et conférenciers spécialisés dans chaque sous-thème ;
    - Volontaires et équipe de soutien ;
    - Autorités et invités des ministères et institutions impliquées.

    Actuellement, **18 institutions brésiliennes** et **18 institutions françaises** sont pré-confirmées,
    travaillant en **paires**.
    """)

    st.subheader("🇧🇷 À propos du Brésil et de Minas Gerais")
    st.markdown("""
    **Brésil :**  
    Plus grand pays d'Amérique du Sud, avec plus de 200 millions d'habitants et une grande diversité culturelle et environnementale.
    Leader mondial de la production agricole, notamment soja, maïs, café, viandes et fruits.
    Il abrite des biomes importants tels que l'Amazonie, le Cerrado et la Mata Atlântica.

    **Minas Gerais :**  
    Deuxième état le plus peuplé du Brésil, avec environ 21 millions d'habitants.  
    Connu pour sa gastronomie, ses beautés naturelles et sa production agricole, en particulier le lait et le café.
    Sa capitale, **Belo Horizonte**, est un important centre politique, économique et culturel.
    """)

    st.subheader("✨ Remarques finales")
    st.markdown("""
    L'édition 2025 sera une **opportunité unique de renforcer les liens de coopération** entre le Brésil et la France.

    Plus qu'un simple événement, le Forum représente une **formation citoyenne, scientifique et culturelle**, 
    préparant les jeunes à relever les défis mondiaux liés à la **durabilité, la sécurité alimentaire et les changements climatiques**.
    """)

# ==============================
# COLUNA EM PORTUGUÊS
# ==============================
with col_br:
    st.info(":green_heart: Versão em português")

    st.markdown("""
    ### 🌎 **Fórum franco-brasileiro Ciência e Sociedade**
    O **Fórum franco-brasileiro Ciência e Sociedade** é uma iniciativa internacional que, desde 2005,
    promove o diálogo entre estudantes, professores, pesquisadores e autoridades do Brasil e da França
    sobre temas de relevância científica e social.  

    O evento ocorre alternadamente entre os dois países e tem como objetivo **estimular o intercâmbio cultural, acadêmico e científico**.

    O ano de **2025** será especialmente simbólico, pois marcará:
    - A **8ª edição** do Fórum,  
    - **20 anos** de sua criação,  
    - E os **200 anos de relações diplomáticas** entre Brasil e França, durante o *Ano do Brasil na França e Ano da França no Brasil*.
    """)

    st.subheader("🎯 Tema e Subtemas")
    st.markdown("""
    **Tema central:**  
    *Sistemas alimentares e mudanças climáticas: desafios e perspectivas*

    Essa escolha reflete os desafios globais enfrentados por ambos os países, especialmente nas áreas de produção agrícola e sustentabilidade ambiental.

    **Subtemas:**
    - 🌱 **Tecnologias e estratégias para uma produção agrícola sustentável:**  
      Soluções técnicas e metodológicas para melhorar a produção sem comprometer o meio ambiente.
    - 💧 **Gestão de recursos naturais:**  
      Estratégias para uso racional e sustentável de recursos como água, solo e adubos orgânicos.
    - 🤝 **Protagonismo individual e coletivo no enfrentamento das alterações climáticas:**  
      O papel da sociedade, comunidades e instituições na construção de soluções para a crise climática.
    """)

    st.subheader("🏛️ Organização e Instituições Envolvidas")
    st.markdown("""
    A **organização** da edição 2025 está a cargo do **Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais (IFMG)**, Brasil, com apoio de parceiros nacionais e internacionais:

    - CONIF – Conselho Nacional das Instituições da Rede Federal (Brasil)
    - SETEC/MEC – Secretaria de Educação Profissional e Tecnológica (Brasil)
    - Ministério da Agricultura e Soberania Alimentar da França (DGER)
    - Réseau Brésil de l’Enseignement Agricole
    - Embaixada da França no Brasil
    - Embrapa – Empresa Brasileira de Pesquisa Agropecuária
    - Ministério do Desenvolvimento Agrário e Agricultura Familiar (Brasil)
    - Ministério da Agricultura e Pecuária (Brasil)

    A **Comissão Organizadora** inclui representantes dos campi IFMG Bambuí, Ouro Preto e Santa Luzia,
    além de membros de outros Institutos Federais e voluntários.
    """)

    st.subheader("📍 Local do Evento")
    st.markdown("""
    A 8ª edição será realizada no **IFMG Campus Bambuí**, localizado a cerca de 270 km de Belo Horizonte.

    Bambuí é uma cidade mineira com aproximadamente **25 mil habitantes**, com economia voltada para a agropecuária.  
    O Campus possui **328,76 hectares** e infraestrutura moderna, com laboratórios, auditórios, áreas experimentais e espaços culturais,
    oferecendo cursos técnicos, de graduação e pós-graduação.

    **Endereço:** Fazenda Varginha, Rodovia Bambuí/Medeiros - km 05, Caixa Postal 05, Bambuí - MG, CEP: 38.900-000.
    """)

    st.subheader("🗓️ Cronograma do Fórum")
    st.markdown("""
    - **Fase de Sensibilização:** até 11/10/2025  
      Desenvolvimento dos projetos conjuntos entre instituições brasileiras e francesas.

    - **Pré-fórum:** 12 a 18/10/2025  
      Delegações francesas visitam suas instituições parceiras no Brasil.

    - **Deslocamento para Bambuí:** 19/10/2025  
      Transporte organizado pela comissão, com recepção no Aeroporto de Confins.

    - **Fórum no IFMG Bambuí:** 20 a 24/10/2025  
      Oficinas técnicas e artísticas, conferências, debates, apresentações culturais e visitas técnicas.

    - **Retorno das delegações:** 25/10/2025  
      Com voos programados para a tarde, a partir das 15h.
    """)

    st.subheader("👥 Público-Alvo")
    st.markdown("""
    O evento reunirá aproximadamente **250 participantes**, incluindo:
    - Professores/formadores e estudantes (1 professor + 4 estudantes por instituição);
    - Pesquisadores e palestrantes especializados em cada subtema;
    - Voluntários e equipe de apoio;
    - Autoridades e convidados dos ministérios e instituições envolvidas.

    Atualmente, estão pré-confirmadas **18 instituições brasileiras** e **18 instituições francesas**, que trabalharão em **pares**.
    """)

    st.subheader("🇧🇷 Sobre o Brasil e Minas Gerais")
    st.markdown("""
    **Brasil:**  
    Maior país da América do Sul, com mais de 200 milhões de habitantes e grande diversidade cultural e ambiental.
    É líder mundial em produção agrícola, destacando-se em soja, milho, café, carnes e frutas.
    Abriga biomas importantes como Amazônia, Cerrado e Mata Atlântica.

    **Minas Gerais:**  
    Segundo estado mais populoso do Brasil, com cerca de 21 milhões de habitantes.  
    Conhecido por sua gastronomia, belezas naturais e produção agrícola, especialmente de leite e café.
    A capital, **Belo Horizonte**, é um importante centro político, econômico e cultural.
    """)

    st.subheader("✨ Considerações Finais")
    st.markdown("""
    A edição 2025 será uma **oportunidade única para fortalecer os laços de cooperação** entre Brasil e França.

    Mais do que um evento, o Fórum representa **formação cidadã, científica e cultural**, preparando jovens para enfrentar desafios globais relacionados à **sustentabilidade, segurança alimentar e mudanças climáticas**.
    """)

# Rodapé
st.markdown("---")
st.markdown("💡 **Desenvolvido por Luciano Vilas Boas Espiridião.**")
st.markdown("[📩 Entre em contato no LinkedIn](https://www.linkedin.com/in/luciano-espiridiao/)")
