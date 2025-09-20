import streamlit as st

# Configuração da página
st.set_page_config(page_title="Programação - Fórum Ciência e Sociedade 2025", page_icon="📅", layout="wide")

# Título principal
st.title("📅 Programação do Fórum Ciência e Sociedade 2025")
st.subheader("Sistemas Alimentares e Mudanças Climáticas: Desafios e Perspectivas")
st.markdown("---")

st.write("""
Abaixo você encontra a programação detalhada do **Fórum Ciência e Sociedade 2025**, 
que acontecerá entre **19 e 25 de outubro de 2025**, no **IFMG Campus Bambuí**, Minas Gerais.
""")

# Lista de dias como abas
dias = [
    "19/10 - Domingo",
    "20/10 - Segunda-feira",
    "21/10 - Terça-feira",
    "22/10 - Quarta-feira",
    "23/10 - Quinta-feira",
    "24/10 - Sexta-feira",
    "25/10 - Sábado"
]

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(dias)

# ------------------------------
with tab1:
    st.header("Domingo - 19 de Outubro")
    st.write("**Atividades previstas para a chegada e integração dos participantes.**")
    st.markdown("""
    - **14h00 em diante:** Chegada dos participantes  
    - Distribuição do material do fórum e programação  
    - Instalação nas acomodações  
    - **Atividades da tarde:**  
      - Visita ao campus  
      - Jogos de integração
    - **18h00 às 19h00:** Jantar  
    - **19h30 às 21h30:** Atividades de integração
    """)

# ------------------------------
with tab2:
    st.header("Segunda-feira - 20 de Outubro")
    st.write("**Visita técnica ao Parque Nacional da Serra da Canastra** *(atividade sujeita a mudanças por questões climáticas)*.")
    st.markdown("""
    - **06h00 às 06h30:** Café da manhã  
    - **06h30:** Saída do grupo  
    - **Manhã:** Visita à Cachoeira Casca D'anta (nascente do Rio São Francisco)  
    - **12h00 às 13h00:** Almoço  
    - **13h00 às 17h00:** Visitas a fazendas produtoras de queijo Canastra (IG Canastra)  
    - **17h00:** Retorno a Bambuí  
    - **19h00 às 20h30:** Jantar  
    - **20h30 às 21h00:** Atividades de integração (livre)
    """)

# ------------------------------
with tab3:
    st.header("Terça-feira - 21 de Outubro")
    st.subheader("Subtema 1: Tecnologias e estratégias para uma produção agrícola sustentável")
    st.markdown("""
    - **07h00 às 08h00:** Café da manhã  
    - **08h30 às 09h50:** Apresentação de **4 equipes** (20 minutos por equipe)  
    - **09h50 às 10h20:** Coffee break  
    - **10h20 às 11h40:** Apresentação de **4 equipes** (20 minutos por equipe)  
    - **12h00 às 14h00:** Almoço  
    - **14h00 às 14h30:** Apresentação artística (definir)  
    - **14h30 às 15h30:** Abertura oficial do Fórum (falas de autoridades)  
    - **15h30 às 16h00:** Conferência - Pesquisador francês  
    - **16h00 às 16h30:** Conferência - Pesquisador brasileiro  
    - **16h30 às 17h00:** Mesa redonda (incluindo perguntas)  
    - **18h00 às 19h00:** Jantar  
    - **19h30 às 21h30:** Sessão de cinema comentado – *ALIMENTERRE*
    """)

# ------------------------------
with tab4:
    st.header("Quarta-feira - 22 de Outubro")
    st.subheader("Subtema 2: Gestão racional de recursos naturais")
    st.markdown("""
    - **07h00 às 08h00:** Café da manhã  
    - **08h00 às 09h30:** Oficinas técnicas (8 oficinas simultâneas)  
    - **09h30 às 10h00:** Coffee break  
    - **10h00 às 12h00:** Oficinas artísticas (8 oficinas simultâneas)  
    - **12h00 às 14h00:** Almoço  
    - **14h00 às 15h00:** Apresentação de **3 equipes** (20 minutos por equipe)  
    - **15h00 às 15h15:** Mini coffee break  
    - **15h15 às 15h45:** Conferência - Pesquisador francês  
    - **15h45 às 16h15:** Conferência - Pesquisador brasileiro  
    - **16h15 às 17h15:** Mesa redonda (incluindo perguntas)  
    - **18h00 às 19h00:** Jantar  
    - **19h30 às 22h00:** Feira cultural e gastronômica na cidade de Bambuí  
      - Apresentações musicais ou teatrais dos estudantes
    """)

# ------------------------------
with tab5:
    st.header("Quinta-feira - 23 de Outubro")
    st.subheader("Subtema 3: Protagonismo do indivíduo no enfrentamento das alterações climáticas")
    st.markdown("""
    - **06h30 às 07h00:** Café da manhã  
    - **Manhã:** Visitas às fazendas no entorno de Bambuí *(atividade sujeita a alterações por questões climáticas)*  
    - **12h00 às 14h00:** Almoço  
    - **14h00 às 15h00:** Apresentação de **3 equipes** (20 minutos por equipe)  
    - **15h00 às 15h15:** Mini coffee break  
    - **15h15 às 15h45:** Conferência - Pesquisador francês  
    - **15h45 às 16h15:** Conferência - Pesquisador brasileiro  
    - **16h15 às 17h15:** Mesa redonda (incluindo perguntas)  
    - **18h00 às 19h00:** Jantar  
    - **19h30 às 22h00:** Fórum livre  
      - Discussões livres sobre temas de interesse dos estudantes
    """)

# ------------------------------
with tab6:
    st.header("Sexta-feira - 24 de Outubro")
    st.subheader("Restituições, compromissos e encerramento")
    st.markdown("""
    - **07h00 às 08h00:** Café da manhã  
    - **08h30 às 09h10:** Apresentação de **2 equipes** (20 minutos por equipe)  
    - **09h10 às 09h30:** Coffee break  
    - **09h30 às 11h30:** Restituição das oficinas técnicas  
      - Espaço comum com boxes, onde equipes apresentam resultados e **compromissos futuros**  
      - Professores redigem a **Carta de Bambuí**, consolidando os compromissos do Fórum
    - **12h00 às 14h00:** Almoço  
    - **14h00 às 14h30:** Apresentação do Serviço Cívico (voluntários franceses)  
    - **14h30 às 16h30:** Restituição coletiva das oficinas artísticas  
    - **16h30 às 17h30:** Encerramento com leitura da **Carta de Bambuí**  
    - **18h00 às 19h00:** Jantar  
    - **19h30:** Festa de encerramento
    """)

# ------------------------------
with tab7:
    st.header("Sábado - 25 de Outubro")
    st.write("**Dia reservado para o retorno das delegações.**")
    st.markdown("""
    - **08h00:** Saída dos ônibus  
    - **Importante:** Voos devem ser agendados **apenas a partir das 15h**, considerando o deslocamento até o Aeroporto de Confins (CNF).
    """)

# Rodapé
st.markdown("---")
st.markdown("💡 **Desenvolvido por Luciano Vilas Boas Espiridião.**")
st.markdown("[📩 Entre em contato no LinkedIn](https://www.linkedin.com/in/luciano-espiridiao/)")
