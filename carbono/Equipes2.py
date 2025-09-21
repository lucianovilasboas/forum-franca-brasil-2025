import streamlit as st

st.set_page_config(page_title="Fórum França-Brasil", page_icon=":earth_americas:", layout="wide")

st.title("👥 Equipes")


st.header("Equipe da Pegada de Carbono")
st.write("Escolas parceiras!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        - 🇫🇷 **Lycée Nature** https://www.lyceenature.com  
    """)

with col2:
    st.markdown("""
        - 🇧🇷 **IFMG - Campus Ponte Nova** https://www.ifmg.edu.br/pontenova
    """)

st.write("---")

st.write("Conheça a equipe de professores e estudantes do Fórum França-Brasil.")


professors = [
    {"name": "Profa. Gaëlle Busson", "country": "França", "role": "Professora", "bio": "..."},
    {"name": "Profa. Patricia  Darjo", "country": "França", "role": "Diretora", "bio": "..."},
    {"name": "Prof. Luciano Espiridião", "country": "Brasil", "role": "Professor de Informática", "bio": "..."},
    {"name": "Prof. Pedro Henrique Pereira", "country": "Brasil", "role": "Professor de íngua Portuguesa", "bio": "..."}
]

students = [
    {"name": "Clara Boissinot", "country": "França", "role": "Estudante", "bio": "Interesse em ciências da computação."},
    {"name": "Martin Cailler", "country": "França", "role": "Estudante", "bio": "Apaixonado por biologia."},
    {"name": "Anaïs Guibert", "country": "França", "role": "Estudante", "bio": "Focado em engenharia."},
    {"name": "Camille Gauthier", "country": "França", "role": "Estudante", "bio": "Interesse em literatura."},

    {"name": "Gabriela Stefany Silva Gomes", "country": "Brasil", "role": "Estudante", "bio": "Interesse em ciências da computação."},
    {"name": "Amanda Guimarães Gomes", "country": "Brasil", "role": "Estudante", "bio": "Apaixonado por biologia."},
    {"name": "Rogério Brandão Bitarães Rocha", "country": "Brasil", "role": "Estudante", "bio": "Focado em engenharia."},
    {"name": "João Pedro Braz Santos", "country": "Brasil", "role": "Estudante", "bio": "Interesse em literatura."}
]

st.header("Professores")
col1, col2 = st.columns(2)
with col1:
    st.subheader("🇫🇷 França")
    for professor in professors:
        if professor["country"] == "França":
            st.subheader(professor["name"])
            st.write(f"**Função:** {professor['role']}")
            st.write(f"**Bio:** {professor['bio']}")
            st.write("---")
with col2:
    st.subheader("🇧🇷 Brasil")
    for professor in professors:
        if professor["country"] == "Brasil":
            st.subheader(professor["name"])
            st.write(f"**Função:** {professor['role']}")
            st.write(f"**Bio:** {professor['bio']}")
            st.write("---")

st.header("Estudantes")
col1, col2 = st.columns(2)
with col1:
    st.subheader("🇫🇷 França")
    for student in students:
        if student["country"] == "França":
            st.subheader(student["name"])
            st.write(f"**Função:** {student['role']}")
            st.write(f"**Bio:** {student['bio']}")
            st.write("---")
with col2:
    st.subheader("🇧🇷 Brasil")
    for student in students:
        if student["country"] == "Brasil":
            st.subheader(student["name"])
            st.write(f"**Função:** {student['role']}")
            st.write(f"**Bio:** {student['bio']}")
            st.write("---")                

