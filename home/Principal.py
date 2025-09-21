import streamlit as st

# ---------------------------------------
# Configuração inicial
# ---------------------------------------
st.set_page_config(
    page_title="Fórum Franco-Brasileiro 2025",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------
# Hero / Cabeçalho
# ---------------------------------------
st.title("🌍 Fórum Franco-Brasileiro Ciência e Sociedade 2025")

col_a, col_b = st.columns([2, 1])
with col_a:
    st.markdown(
        """
        <div style='font-size:1.05rem;'>
        Bienvenue • Bem-vindos!<br/>
        Reunindo estudantes, professores e pesquisadores do Brasil e da França para dialogar sobre <b>sistemas alimentares</b> e <b>mudanças climáticas</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("📍 <b>Local:</b> IFMG Campus Bambuí — Minas Gerais, Brasil", unsafe_allow_html=True)
    st.markdown("📅 <b>Data:</b> 20 a 24 de outubro de 2025", unsafe_allow_html=True)

with col_b:
    # Atalhos rápidos para páginas internas
    st.markdown("#### 🔗 Acesso rápido")
    st.page_link("home/Forum.py", label="Sobre o Fórum", icon="📘")
    st.page_link("home/Programacao.py", label="Programação", icon="📅")
    st.page_link("home/Ods.py", label="ODS (Objetivos do Desenvolvimento Sustentável)", icon="🎯")

st.markdown("---")

st.markdown("🌐 Site oficial: https://francabrasil2025.com/")

st.markdown("---")


# ---------------------------------------
# Métricas resumidas
# ---------------------------------------
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="Participantes previstos", value="≈ 250")
with col_m2:
    st.metric(label="Instituições parceiras", value="36", delta="18 BR • 18 FR")
with col_m3:
    st.metric(label="Edição", value="8ª", delta="2005 → 2025")

st.markdown("---")

# ---------------------------------------
# Galeria de fotos (arquivos existentes em images/)
# ---------------------------------------
st.subheader("📸 Destaques do Local e Região")

# Linha 1: destaque (imagem ampla)
st.image(
    "images/Campus_Bambui.png",
    caption="IFMG Campus Bambuí",
    use_container_width=True,
)

# Linha 2: duas colunas
c1, c2 = st.columns([5, 6])
with c1:
    st.image(
        "images/Brasil__Rio_de_Janeiro__Natureza__Arquitetura.png",
        caption="Paisagens do Brasil",
        use_container_width=True,
    )

with c2:
    st.image(
        "images/Mapa_Minas_Gearis__Bambui.png",
        caption="Mapa de Minas Gerais e Bambuí",
        use_container_width=True,
    )

# Linha 3: duas colunas
c3, c4 = st.columns([2,3])
with c3:
    st.image(
        "images/Minas_Gerais__Gastronomia__Ouro_Preto_Paisagens.png",
        caption="Cultura e gastronomia mineira",
        use_container_width=True,
    )    

with c4:
    st.image(
        "images/Sao_Roque_de_Minas.png",
        caption="Serra da Canastra e entorno",
        use_container_width=True,
    )    


# ---------------------------------------
# Rodapé
# ---------------------------------------
st.markdown("---")
st.caption("🌱 Desenvolvido para o Fórum Franco-Brasileiro 2025 | IFMG Campus Bambuí")
