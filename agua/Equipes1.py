import streamlit as st

st.set_page_config(page_title="Fórum França-Brasil", page_icon=":earth_americas:", layout="wide")


st.title("👥 Equipes")

st.header("Equipe do Ciclo da Água")
st.write("Conheça a equipe de professores e estudantes do Fórum França-Brasil.")
st.write("---")

professors = [
    {"name": "Prof. Pierre", "country": "França", "role": "Professor de Matemática", "bio": "Especialista em álgebra e geometria."},
    {"name": "Prof. João", "country": "Brasil", "role": "Professor de Física", "bio": "Focado em mecânica quântica e termodinâmica."}
]

students = [
    {"name": "Étudiant 1", "country": "França", "role": "Estudante", "bio": "Interesse em ciências da computação."},
    {"name": "Étudiant 2", "country": "França", "role": "Estudante", "bio": "Apaixonado por biologia."},
    {"name": "Étudiant 3", "country": "França", "role": "Estudante", "bio": "Focado em engenharia."},
    {"name": "Étudiant 4", "country": "França", "role": "Estudante", "bio": "Interesse em literatura."},
    {"name": "Estudante 1", "country": "Brasil", "role": "Estudante", "bio": "Interesse em ciências da computação."},
    {"name": "Estudante 2", "country": "Brasil", "role": "Estudante", "bio": "Apaixonado por biologia."},
    {"name": "Estudante 3", "country": "Brasil", "role": "Estudante", "bio": "Focado em engenharia."},
    {"name": "Estudante 4", "country": "Brasil", "role": "Estudante", "bio": "Interesse em literatura."}
]

st.header("Professores")
col1, col2 = st.columns(2)
with col1:
    st.subheader("França")
    for professor in professors:
        if professor["country"] == "França":
            st.subheader(professor["name"])
            st.write(f"**Função:** {professor['role']}")
            st.write(f"**Bio:** {professor['bio']}")
            st.write("---")
with col2:
    st.subheader("Brasil")
    for professor in professors:
        if professor["country"] == "Brasil":
            st.subheader(professor["name"])
            st.write(f"**Função:** {professor['role']}")
            st.write(f"**Bio:** {professor['bio']}")
            st.write("---")

st.header("Estudantes")
col1, col2 = st.columns(2)
with col1:
    st.subheader("França")
    for student in students:
        if student["country"] == "França":
            st.subheader(student["name"])
            st.write(f"**Função:** {student['role']}")
            st.write(f"**Bio:** {student['bio']}")
            st.write("---")
with col2:
    st.subheader("Brasil")
    for student in students:
        if student["country"] == "Brasil":
            st.subheader(student["name"])
            st.write(f"**Função:** {student['role']}")
            st.write(f"**Bio:** {student['bio']}")
            st.write("---")



