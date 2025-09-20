import streamlit as st
import pandas as pd
import sqlite3
import user

# Conexão com o banco de dados SQLite
conn = sqlite3.connect(user.database_name)
cursor = conn.cursor()

# Criar tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS acoes (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    descricao TEXT,
    ods TEXT,
    campus TEXT,
    status TEXT,
    indicadores TEXT,
    data_inicio TEXT,
    data_fim TEXT,
    responsaveis TEXT
)
''')
conn.commit()

# Lista com os ODS
lista_ods = [
    "1 - Erradicação da Pobreza",
    "2 - Fome Zero e Agricultura Sustentável",
    "3 - Saúde e Bem-Estar",
    "4 - Educação de Qualidade",
    "5 - Igualdade de Gênero",
    "6 - Água Potável e Saneamento",
    "7 - Energia Acessível e Limpa",
    "8 - Trabalho Decente e Crescimento Econômico",
    "9 - Indústria, Inovação e Infraestrutura",
    "10 - Redução das Desigualdades",
    "11 - Cidades e Comunidades Sustentáveis",
    "12 - Consumo e Produção Responsáveis",
    "13 - Ação Contra a Mudança Global do Clima",
    "14 - Vida na Água",
    "15 - Vida Terrestre",
    "16 - Paz, Justiça e Instituições Eficazes",
    "17 - Parcerias e Meios de Implementação"
]

# Título do app
st.title("Monitor de Ações de Sustentabilidade")

# Menu lateral
menu = st.sidebar.selectbox("Menu", ["Cadastrar Ação", "Visualizar Ações", "Indicadores"])

# Cadastro de Ações
if menu == "Cadastrar Ação":
    st.subheader("Cadastrar Nova Ação")
    with st.form(key="cadastro"):
        titulo = st.text_input("Título da Ação")
        descricao = st.text_area("Descrição")
        ods_selecionados = st.multiselect("ODS Relacionados", lista_ods)
        campus = st.selectbox("Campus", [
            "Reitoria", "Arcos", "Bambuí", "Betim", "Congonhas", "Conselheiro Lafaiete", "Formiga", 
            "Governador Valadares", "Ibirité", "Ipatinga", "Itabirito", 
            "Sabará", "Santa Luzia", "Ribeirão das Neves", "Ponte Nova",
            "Ouro Branco", "Ouro Preto", "São João Evangelista"
        ])
        status = st.selectbox("Status", ["Planejada", "Em Andamento", "Concluída"])
        indicadores = st.text_area("Indicadores (ex.: Redução de 10% de consumo de energia)")
        data_inicio = st.date_input("Data de Início")
        data_fim = st.date_input("Data de Término")
        responsaveis = st.text_input("Responsáveis")
        submit = st.form_submit_button("Cadastrar")
        
        if submit:
            ods = ", ".join(ods_selecionados)  # Transformar a lista de ODS em string
            cursor.execute('''
            INSERT INTO acoes (titulo, descricao, ods, campus, status, indicadores, data_inicio, data_fim, responsaveis)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (titulo, descricao, ods, campus, status, indicadores, data_inicio, data_fim, responsaveis))
            conn.commit()
            st.success("Ação cadastrada com sucesso!")

# Visualizar Ações
elif menu == "Visualizar Ações":
    st.subheader("Ações Cadastradas")
    data = pd.read_sql_query("SELECT * FROM acoes", conn)
    if not data.empty:
        st.dataframe(data)
    else:
        st.warning("Nenhuma ação cadastrada no momento.")

# Indicadores
elif menu == "Indicadores":
    st.subheader("Indicadores de Sustentabilidade")
    data = pd.read_sql_query("SELECT campus, COUNT(*) as total_acoes FROM acoes GROUP BY campus", conn)
    if not data.empty:
        st.bar_chart(data.set_index("campus"))
    else:
        st.warning("Ainda não há dados suficientes para exibir indicadores.")
