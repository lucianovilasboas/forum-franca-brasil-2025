import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# Configuração inicial
# ----------------------------
st.set_page_config(
    page_title="Calculadora de Pegada de Carbono Escolar",
    page_icon="🌱",
    layout="wide"
)

st.title("🌍 Calculadora de Pegada de Carbono Escolar")
st.markdown("""
Esta ferramenta estima a **pegada de carbono anual (t CO₂e/ano)** da sua escola com base em informações de transporte, 
energia, água, geração de lixo, pessoas e medidas de compensação.  
Preencha os campos abaixo para visualizar os resultados.
""")

# ----------------------------
# Entradas do usuário
# ----------------------------
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

# Pessoas e computadores
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

# Detalhes adicionais
# st.subheader("📋 Mais Detalhes")
# infra_convivencia = st.text_area("Infraestrutura de convivência (refeitórios, áreas comuns, etc.)")
# funcionamento = st.text_area("Funcionamento (turnos, horários e períodos de maior movimento)")

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

st.markdown("---")

# ----------------------------
# Cálculos
# ----------------------------
if st.button("Calcular Pegada de Carbono"):
    # Fatores de emissão aproximados (simplificados)
    fator_combustivel = 2.31  # kg CO2e por litro de gasolina
    fator_energia = 0.084     # kg CO2e por kWh (Brasil, matriz majoritariamente limpa)
    fator_agua = 0.0003       # kg CO2e por litro (tratamento e bombeamento)
    fator_lixo = 1.9          # kg CO2e por kg de lixo comum
    fator_arvore = 22         # kg CO2e sequestrados por árvore/ano

    # Transporte (litros/mês * fator * 12 meses)
    emissao_transporte = consumo_combustivel * fator_combustivel * 12

    # Energia (kWh/mês * fator * 12 meses)
    emissao_energia = consumo_energia * fator_energia * 12

    # Água (litros/mês * fator * 12 meses)
    emissao_agua = consumo_agua * fator_agua * 12

    # Lixo (kg/mês * fator * 12 meses)
    emissao_lixo = volume_lixo * fator_lixo * 12

    # Emissões totais (kg CO2e/ano)
    emissao_total_kg = emissao_transporte + emissao_energia + emissao_agua + emissao_lixo

    # Converter para toneladas
    emissao_total_t = emissao_total_kg / 1000

    # Compensação por árvores
    compensacao_kg = arvores * fator_arvore
    emissao_liquida_t = (emissao_total_kg - compensacao_kg) / 1000

    # ----------------------------
    # Resultados
    # ----------------------------
    st.success(f"🌱 **Pegada de carbono estimada (total): {emissao_total_t:.2f} t CO₂e/ano**")
    st.info(f"Após compensação por árvores: **{emissao_liquida_t:.2f} t CO₂e/ano**")

    # Gráfico de pizza
    data = {
        "Setor": ["Transporte", "Energia", "Água", "Lixo"],
        "Emissões (kg CO₂e/ano)": [emissao_transporte, emissao_energia, emissao_agua, emissao_lixo]
    }
    df = pd.DataFrame(data)

    fig = px.pie(df, values="Emissões (kg CO₂e/ano)", names="Setor", title="Distribuição das Emissões por Setor",
                 color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)

    # Tabela detalhada
    st.subheader("📊 Relatório Detalhado")
    st.table(df.style.format({"Emissões (kg CO₂e/ano)": "{:.2f}"}))

    st.markdown("---")
    st.markdown("""
    ### Fórmulas utilizadas:
    - **Transporte:** Consumo (L/mês) × 2,31 × 12  
    - **Energia:** Consumo (kWh/mês) × 0,084 × 12  
    - **Água:** Consumo (L/mês) × 0,0003 × 12  
    - **Lixo:** Geração (kg/mês) × 1,9 × 12  
    - **Árvores:** Cada árvore compensa **22 kg CO₂e/ano**
    """)

    st.caption("⚠️ Valores aproximados para estimativas iniciais. Para inventários oficiais, siga GHG Protocol e normas ISO 14064/14067.")
