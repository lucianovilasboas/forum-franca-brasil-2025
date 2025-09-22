import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------
# Configuração inicial
# ---------------------------------------
st.set_page_config(
    page_title="Calculadora de Pegada de Carbono Escolar",
    page_icon="🌱",
    layout="wide"
)

st.title("🌍 Calculadora de Pegada de Carbono Escolar")
st.markdown("""
Esta ferramenta estima a **pegada de carbono anual (t CO₂e/ano)** da sua escola considerando:
- Transporte institucional
- Consumo de energia e água
- Geração de resíduos
- Número de pessoas (funcionários e estudantes)
- Infraestrutura física
- Compensações (plantio de árvores e medidas adicionais)

Os cálculos são baseados em **fatores de emissão médios** de fontes como **IPCC**, **EPA**, **GHG Protocol** e **ANEEL**.
""")

# ---------------------------------------
# Entradas
# ---------------------------------------
st.header("📌 Informações da Escola")
col1, col2, col3 = st.columns(3)
with col1:
    nome_escola = st.text_input("Nome da escola", placeholder="Informe o nome da escola")
with col2:
    municipio_escola = st.text_input("Município", placeholder="Informe o município")
with col3:
    pais = st.selectbox("País", ["Brasil", "França", "Outro"], index=0)

# Transporte institucional
st.subheader("🚐 Transporte Institucional")
col1, col2, col3 = st.columns(3)
with col1:
    num_veiculos = st.number_input("Número de veículos", min_value=0, step=1)
with col2:
    num_viagens_mes = st.number_input("Número de viagens por mês", min_value=0, step=1)
with col3:
    consumo_combustivel = st.number_input("Consumo mensal de combustível (litros)", min_value=0.0, step=0.1)

# Pessoas
st.subheader("👩‍🏫 Pessoas")
col1, col2 = st.columns(2)
with col1:
    num_funcionarios = st.number_input("Número de funcionários", min_value=0, step=1)
with col2:
    num_estudantes = st.number_input("Número de estudantes", min_value=0, step=1)

# Infraestrutura
st.subheader("🏫 Infraestrutura")
col1, col2, col3, col4 = st.columns(4)
with col1:
    num_salas_aula = st.number_input("Salas de aula", min_value=0, step=1)
with col2:
    num_salas_adm = st.number_input("Salas administrativas", min_value=0, step=1)
with col3:
    num_laboratorios = st.number_input("Laboratórios", min_value=0, step=1)
with col4:
    num_auditorios = st.number_input("Auditórios", min_value=0, step=1)

# Energia
st.subheader("⚡ Energia")
col1, col2, col3 = st.columns(3)
with col1:
    consumo_energia = st.number_input("Consumo médio mensal (kWh)", min_value=0.0, step=0.1)
with col2:
    possui_geracao_propria = st.selectbox("Possui geração própria de energia?", ["Não", "Sim"])
with col3:
    geracao_energia = st.text_input("Tipo e quantidade gerada mensalmente (kWh)", placeholder="Ex: Solar, 500 kWh/mês")

# Água
st.subheader("💧 Água")
consumo_agua = st.number_input("Consumo médio mensal de água (litros)", min_value=0.0, step=10.0)

# Lixo
st.subheader("🗑️ Geração de Lixo")
volume_lixo = st.number_input("Volume de lixo gerado por mês (kg)", min_value=0.0, step=1.0)

# Compensação
st.subheader("🌳 Medidas de Compensação")
arvores = st.number_input("Árvores plantadas", min_value=0, step=1)

st.markdown("#### Outras Medidas Customizadas")
st.caption("Estime a quantidade de CO₂e evitada ou reduzida por cada ação (em kg CO₂e/ano).")

col1, col2 = st.columns(2)
with col1:
    meliponario = st.number_input("🐝 Criação de meliponário no campus", min_value=0.0, step=1.0, help="Melhora da biodiversidade e sequestro indireto de carbono")
    reducao_agua = st.number_input("💧 Redução no gasto com água", min_value=0.0, step=1.0, help="Ex: Uso de cisternas, reúso de água")
    reducao_energia = st.number_input("⚡ Redução no gasto com energia", min_value=0.0, step=1.0, help="Ex: Instalação de painéis solares")
with col2:
    otimizacao_viagens = st.number_input("🚐 Otimização de viagens", min_value=0.0, step=1.0, help="Ex: Melhor planejamento de rotas e transporte coletivo")
    reducao_lixo = st.number_input("🗑️ Redução de lixo produzido", min_value=0.0, step=1.0, help="Ex: Compostagem, reciclagem")

st.markdown("---")

# ---------------------------------------
# Cálculos
# ---------------------------------------
if st.button("Calcular Pegada de Carbono"):
    # --- Fatores de emissão aproximados ---
    fator_combustivel = 2.31  # kg CO2e/litro
    fator_energia = 0.084     # kg CO2e/kWh
    fator_agua = 0.0003       # kg CO2e/litro
    fator_lixo = 1.9          # kg CO2e/kg lixo
    fator_arvore = 22         # kg CO2e/árvore/ano
    fator_pessoa = 500        # kg CO2e/pessoa/ano

    # Infraestrutura: estimativa
    fator_sala_aula = 150
    fator_sala_adm = 100
    fator_lab = 300
    fator_auditorio = 500

    # --- Cálculo por setor ---
    emissao_transporte = consumo_combustivel * fator_combustivel * 12
    emissao_energia = consumo_energia * fator_energia * 12
    emissao_agua = consumo_agua * fator_agua * 12
    emissao_lixo = volume_lixo * fator_lixo * 12
    total_pessoas = num_funcionarios + num_estudantes
    emissao_pessoas = total_pessoas * fator_pessoa
    emissao_infra = (
        num_salas_aula * fator_sala_aula +
        num_salas_adm * fator_sala_adm +
        num_laboratorios * fator_lab +
        num_auditorios * fator_auditorio
    )

    # --- Total e compensação ---
    emissao_total_kg = (
        emissao_transporte + emissao_energia + emissao_agua +
        emissao_lixo + emissao_pessoas + emissao_infra
    )

    # Compensações customizadas
    compensacoes_custom_kg = (
        meliponario +
        reducao_agua +
        reducao_energia +
        otimizacao_viagens +
        reducao_lixo
    )

    # Compensação total
    compensacao_kg = (arvores * fator_arvore) + compensacoes_custom_kg
    emissao_liquida_t = (emissao_total_kg - compensacao_kg) / 1000
    emissao_total_t = emissao_total_kg / 1000

    # ---------------------------------------
    # Resultados
    # ---------------------------------------
    st.success(f"🌱 **Pegada de carbono estimada (total): {emissao_total_t:.2f} t CO₂e/ano**")
    st.info(f"Após compensações (árvores + customizadas): **{emissao_liquida_t:.2f} t CO₂e/ano**")

    # ---------------------------------------
    # Gráficos
    # ---------------------------------------
    data = {
        "Setor": [
            "Transporte", "Energia", "Água", "Lixo",
            "Pessoas (funcionários + estudantes)",
            "Infraestrutura"
        ],
        "Emissões (kg CO₂e/ano)": [
            emissao_transporte, emissao_energia, emissao_agua,
            emissao_lixo, emissao_pessoas, emissao_infra
        ]
    }
    df = pd.DataFrame(data)

    col1, col2 = st.columns([2, 1])
    with col1:
        fig = px.pie(
            df,
            values="Emissões (kg CO₂e/ano)",
            names="Setor",
            title="Distribuição das Emissões por Setor",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("Resumo Numérico")
        st.dataframe(df.style.format({"Emissões (kg CO₂e/ano)": "{:.2f}"}))

    # ---------------------------------------
    # Relatório Detalhado
    # ---------------------------------------
    st.markdown("---")
    st.subheader("📊 Relatório Detalhado")

    st.markdown(f"""
    ### Resumo geral
    - **Nome da Escola:** {nome_escola}
    - **Município:** {municipio_escola}
    - **País:** {pais}
    - **Total de pessoas:** {total_pessoas} (Funcionários: {num_funcionarios}, Estudantes: {num_estudantes})
    - **Emissões totais (sem compensações):** {emissao_total_t:.2f} t CO₂e/ano
    - **Compensação total:** {compensacao_kg/1000:.2f} t CO₂e/ano
    - **Emissões líquidas:** {emissao_liquida_t:.2f} t CO₂e/ano
    """)

    st.markdown("### Detalhes das compensações customizadas")
    st.markdown(f"""
    - **Criação de meliponário:** {meliponario:.2f} kg CO₂e/ano  
    - **Redução no gasto com água:** {reducao_agua:.2f} kg CO₂e/ano  
    - **Redução no gasto com energia:** {reducao_energia:.2f} kg CO₂e/ano  
    - **Otimização de viagens:** {otimizacao_viagens:.2f} kg CO₂e/ano  
    - **Redução de lixo produzido:** {reducao_lixo:.2f} kg CO₂e/ano  
    """)

    st.markdown("### Observações")
    st.caption("""
    ⚠️ Os valores das compensações customizadas devem ser informados manualmente, 
    com base em estudos ou estimativas locais.  
    Essa flexibilidade permite incluir projetos inovadores e adaptações específicas de cada campus.
    """)

    st.markdown("### Fórmulas utilizadas")
    st.markdown("""
    - **Transporte:** Consumo mensal (L) × 2,31 × 12  
    - **Energia:** Consumo mensal (kWh) × 0,084 × 12  
    - **Água:** Consumo mensal (L) × 0,0003 × 12  
    - **Lixo:** Volume mensal (kg) × 1,9 × 12  
    - **Pessoas:** Total de pessoas × 500 kg CO₂e/ano  
    - **Compensação total:** Árvores × 22 + Somatório das compensações customizadas
    """)

    st.write("---")
    st.caption("⚠️ Essa calculadora é um protótipo educacional. Para inventários oficiais, siga o GHG Protocol e a ISO 14064/14067.")
