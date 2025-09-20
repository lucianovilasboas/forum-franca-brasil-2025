import streamlit as st

# Configuração da página
st.set_page_config(page_title="Programação - Fórum Ciência e Sociedade 2025", page_icon="📅", layout="wide")

# Título principal
col_fr_title, col_br_title = st.columns(2)
with col_fr_title:
    st.title("📅 Programme")
with col_br_title:
    st.title("📅 Programação")

col_fr, col_br = st.columns(2)

col_fr.subheader("🇫🇷 Systèmes Alimentaires et Changements Climatiques : Défis et Perspectives")
col_br.subheader("🌱 Sistemas Alimentares e Mudanças Climáticas: Desafios e Perspectivas")

st.markdown("---")

col_fr_desc, col_br_desc = st.columns(2)

with col_fr_desc:
    st.write("""
    Abaixo você encontra a programação detalhada do **Fórum Ciência e Sociedade 2025**, 
    que acontecerá entre **19 e 25 de outubro de 2025**, no **IFMG Campus Bambuí**, Minas Gerais.
    """)

with col_br_desc:
    st.write("""
    Ci-dessous, vous trouverez le programme détaillé du **Forum Science et Société 2025**, 
    qui se déroulera du **19 au 25 octobre 2025**, sur le **campus IFMG de Bambuí**, Minas Gerais.
    """)



# Lista de dias como abas
dias = [
    "19/10 - Domingo / Dimanche",
    "20/10 - Segunda-feira / Lundi",
    "21/10 - Terça-feira / Mardi",
    "22/10 - Quarta-feira / Mercredi",
    "23/10 - Quinta-feira / Jeudi",
    "24/10 - Sexta-feira / Vendredi",
    "25/10 - Sábado / Samedi"
]

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(dias)

# Função auxiliar para duas colunas
def duas_colunas(conteudo_br, conteudo_fr):
    col_fr, col_br = st.columns(2)
    with col_fr:
        st.markdown("### 🇫🇷 **Programme en Français**")
        st.markdown(conteudo_fr)
    with col_br:
        st.markdown("### 🇧🇷 **Programação em Português**")
        st.markdown(conteudo_br)

# ------------------------------
with tab1:
    st.header("🚌 Domingo / Dimanche - 19/10")
    duas_colunas(
        """
        **Atividades previstas para a chegada e integração dos participantes:**

        - **14h00 em diante:** Chegada dos participantes  
        - Distribuição do material do fórum e programação  
        - Instalação nas acomodações  
        - **Atividades da tarde:**  
          - Visita ao campus  
          - Jogos de integração  
        - **18h00 às 19h00:** Jantar  
        - **19h30 às 21h30:** Atividades de integração  
        """,
        """
        **Activités prévues pour l'arrivée et l'intégration des participants :**

        - **À partir de 14h00 :** Arrivée des participants  
        - Distribution du matériel du forum et du programme  
        - Installation dans les hébergements  
        - **Activités de l'après-midi :**  
          - Visite du campus  
          - Jeux d'intégration  
        - **18h00 à 19h00 :** Dîner  
        - **19h30 à 21h30 :** Activités d'intégration  
        """
    )

# ------------------------------
with tab2:
    st.header("🏞️ Segunda-feira / Lundi - 20/10")
    duas_colunas(
        """
        **Visita técnica ao Parque Nacional da Serra da Canastra**  
        *(atividade sujeita a mudanças por questões climáticas)*

        - **06h00 às 06h30:** Café da manhã  
        - **06h30:** Saída do grupo  
        - **Manhã:** Visita à Cachoeira Casca D'anta (nascente do Rio São Francisco)  
        - **12h00 às 13h00:** Almoço  
        - **13h00 às 17h00:** Visitas a fazendas produtoras de queijo Canastra (IG Canastra)  
        - **17h00:** Retorno a Bambuí  
        - **19h00 às 20h30:** Jantar  
        - **20h30 às 21h00:** Atividades de integração (livre)  
        """,
        """
        **Visite technique au Parc National de la Serra da Canastra**  
        *(activité sujette à modification en fonction des conditions météorologiques)*

        - **06h00 à 06h30 :** Petit déjeuner  
        - **06h30 :** Départ du groupe  
        - **Matin :** Visite de la cascade Casca D'anta (source du Rio São Francisco)  
        - **12h00 à 13h00 :** Déjeuner  
        - **13h00 à 17h00 :** Visite des fermes productrices du fromage Canastra (IG Canastra)  
        - **17h00 :** Retour à Bambuí  
        - **19h00 à 20h30 :** Dîner  
        - **20h30 à 21h00 :** Activités d'intégration (libres)  
        """
    )

# ------------------------------
with tab3:
    st.header("🌱 Terça-feira / Mardi - 21/10")
    duas_colunas(
        """
        **Subtema 1: Tecnologias e estratégias para uma produção agrícola sustentável**

        - **07h00 às 08h00:** Café da manhã  
        - **08h30 às 09h50:** Apresentação de **4 equipes** (20 min por equipe)  
        - **09h50 às 10h20:** Coffee break  
        - **10h20 às 11h40:** Apresentação de **4 equipes** (20 min por equipe)  
        - **12h00 às 14h00:** Almoço  
        - **14h00 às 14h30:** Apresentação artística  
        - **14h30 às 15h30:** Abertura oficial do Fórum  
        - **15h30 às 16h00:** Conferência - Pesquisador francês  
        - **16h00 às 16h30:** Conferência - Pesquisador brasileiro  
        - **16h30 às 17h00:** Mesa redonda (com perguntas)  
        - **18h00 às 19h00:** Jantar  
        - **19h30 às 21h30:** Sessão de cinema comentado – *ALIMENTERRE*  
        """,
        """
        **Sous-thème 1 : Technologies et stratégies pour une production agricole durable**

        - **07h00 à 08h00 :** Petit déjeuner  
        - **08h30 à 09h50 :** Présentation de **4 équipes** (20 min par équipe)  
        - **09h50 à 10h20 :** Pause café  
        - **10h20 à 11h40 :** Présentation de **4 équipes** (20 min par équipe)  
        - **12h00 à 14h00 :** Déjeuner  
        - **14h00 à 14h30 :** Présentation artistique  
        - **14h30 à 15h30 :** Ouverture officielle du Forum  
        - **15h30 à 16h00 :** Conférence - Chercheur français  
        - **16h00 à 16h30 :** Conférence - Chercheur brésilien  
        - **16h30 à 17h00 :** Table ronde (avec questions)  
        - **18h00 à 19h00 :** Dîner  
        - **19h30 à 21h30 :** Séance de cinéma commentée – *ALIMENTERRE*  
        """
    )

# ------------------------------
with tab4:
    st.header("💧 Quarta-feira / Mercredi - 22/10")
    duas_colunas(
        """
        **Subtema 2: Gestão racional de recursos naturais**

        - **07h00 às 08h00:** Café da manhã  
        - **08h00 às 09h30:** Oficinas técnicas (8 simultâneas)  
        - **09h30 às 10h00:** Coffee break  
        - **10h00 às 12h00:** Oficinas artísticas (8 simultâneas)  
        - **12h00 às 14h00:** Almoço  
        - **14h00 às 15h00:** Apresentação de **3 equipes** (20 min por equipe)  
        - **15h00 às 15h15:** Mini coffee break  
        - **15h15 às 15h45:** Conferência - Pesquisador francês  
        - **15h45 às 16h15:** Conferência - Pesquisador brasileiro  
        - **16h15 às 17h15:** Mesa redonda (com perguntas)  
        - **18h00 às 19h00:** Jantar  
        - **19h30 às 22h00:** Feira cultural e gastronômica na cidade de Bambuí  
          - Apresentações musicais e teatrais dos estudantes  
        """,
        """
        **Sous-thème 2 : Gestion rationnelle des ressources naturelles**

        - **07h00 à 08h00 :** Petit déjeuner  
        - **08h00 à 09h30 :** Ateliers techniques (8 simultanés)  
        - **09h30 à 10h00 :** Pause café  
        - **10h00 à 12h00 :** Ateliers artistiques (8 simultanés)  
        - **12h00 à 14h00 :** Déjeuner  
        - **14h00 à 15h00 :** Présentation de **3 équipes** (20 min par équipe)  
        - **15h00 à 15h15 :** Mini pause café  
        - **15h15 à 15h45 :** Conférence - Chercheur français  
        - **15h45 à 16h15 :** Conférence - Chercheur brésilien  
        - **16h15 à 17h15 :** Table ronde (avec questions)  
        - **18h00 à 19h00 :** Dîner  
        - **19h30 à 22h00 :** Foire culturelle et gastronomique dans la ville de Bambuí  
          - Présentations musicales et théâtrales des étudiants  
        """
    )

# ------------------------------
with tab5:
    st.header("🤝 Quinta-feira / Jeudi - 23/10")
    duas_colunas(
        """
        **Subtema 3: Protagonismo do indivíduo no enfrentamento das alterações climáticas**

        - **06h30 às 07h00:** Café da manhã  
        - **Manhã:** Visitas às fazendas ao redor de Bambuí *(atividade sujeita a alterações climáticas)*  
        - **12h00 às 14h00:** Almoço  
        - **14h00 às 15h00:** Apresentação de **3 equipes** (20 min por equipe)  
        - **15h00 às 15h15:** Mini coffee break  
        - **15h15 às 15h45:** Conferência - Pesquisador francês  
        - **15h45 às 16h15:** Conferência - Pesquisador brasileiro  
        - **16h15 às 17h15:** Mesa redonda (com perguntas)  
        - **18h00 às 19h00:** Jantar  
        - **19h30 às 22h00:** Fórum livre - Discussões abertas com estudantes  
        """,
        """
        **Sous-thème 3 : Rôle de l'individu dans la lutte contre les changements climatiques**

        - **06h30 à 07h00 :** Petit déjeuner  
        - **Matin :** Visites des fermes autour de Bambuí *(activité sujette à modifications climatiques)*  
        - **12h00 à 14h00 :** Déjeuner  
        - **14h00 à 15h00 :** Présentation de **3 équipes** (20 min par équipe)  
        - **15h00 à 15h15 :** Mini pause café  
        - **15h15 à 15h45 :** Conférence - Chercheur français  
        - **15h45 à 16h15 :** Conférence - Chercheur brésilien  
        - **16h15 à 17h15 :** Table ronde (avec questions)  
        - **18h00 à 19h00 :** Dîner  
        - **19h30 à 22h00 :** Forum libre - Discussions ouvertes avec les étudiants  
        """
    )

# ------------------------------
with tab6:
    st.header("✨ Sexta-feira / Vendredi - 24/10")
    duas_colunas(
        """
        **Restituições, compromissos e encerramento**

        - **07h00 às 08h00:** Café da manhã  
        - **08h30 às 09h10:** Apresentação de **2 equipes** (20 min por equipe)  
        - **09h10 às 09h30:** Coffee break  
        - **09h30 às 11h30:** Restituição das oficinas técnicas  
          - Espaço com boxes, onde equipes apresentam resultados e **compromissos futuros**  
          - Professores redigem a **Carta de Bambuí**  
        - **12h00 às 14h00:** Almoço  
        - **14h00 às 14h30:** Apresentação do Serviço Cívico (voluntários franceses)  
        - **14h30 às 16h30:** Restituição coletiva das oficinas artísticas  
        - **16h30 às 17h30:** Leitura da **Carta de Bambuí**  
        - **18h00 às 19h00:** Jantar  
        - **19h30:** Festa de encerramento  
        """,
        """
        **Restitutions, engagements et clôture**

        - **07h00 à 08h00 :** Petit déjeuner  
        - **08h30 à 09h10 :** Présentation de **2 équipes** (20 min par équipe)  
        - **09h10 à 09h30 :** Pause café  
        - **09h30 à 11h30 :** Restitution des ateliers techniques  
          - Stands où les équipes présentent leurs résultats et **engagements futurs**  
          - Rédaction de la **Lettre de Bambuí** par les enseignants  
        - **12h00 à 14h00 :** Déjeuner  
        - **14h00 à 14h30 :** Présentation du Service Civique (volontaires français)  
        - **14h30 à 16h30 :** Restitution collective des ateliers artistiques  
        - **16h30 à 17h30 :** Lecture de la **Lettre de Bambuí**  
        - **18h00 à 19h00 :** Dîner  
        - **19h30 :** Fête de clôture  
        """
    )

# ------------------------------
with tab7:
    st.header("✈️ Sábado / Samedi - 25/10")
    duas_colunas(
        """
        **Dia reservado para o retorno das delegações**

        - **08h00:** Saída dos ônibus  
        - **Importante:** Voos devem ser agendados **apenas a partir das 15h**, considerando o deslocamento até o Aeroporto de Confins (CNF).
        """,
        """
        **Journée réservée au retour des délégations**

        - **08h00 :** Départ des bus  
        - **Important :** Les vols doivent être programmés **uniquement à partir de 15h**, en tenant compte du trajet jusqu'à l'aéroport de Confins (CNF).
        """
    )

# Rodapé
st.markdown("---")
st.markdown("💡 **Desenvolvido por Luciano Vilas Boas Espiridião.**")
st.markdown("[📩 Entre em contato no LinkedIn](https://www.linkedin.com/in/luciano-espiridiao/)")
