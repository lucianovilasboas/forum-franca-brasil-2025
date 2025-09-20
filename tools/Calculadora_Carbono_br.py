import streamlit as st
import math

st.set_page_config(page_title="Fórum França-Brasil", page_icon=":earth_americas:", layout="wide")

def calcular_equivalencia_arvores(emissao_total):
    # Aproximadamente uma árvore absorve 21 kg de CO2 por ano
    return emissao_total / 21

def calcular_equivalencia_carros(emissao_total):
    # Um carro emite cerca de 12000 kg de CO2 por ano
    return emissao_total / 12000


st.title(":deciduous_tree: Calculadora de Pegada de Carbono :earth_africa:")
st.markdown("""
## Estime suas emissões e descubra seu impacto no planeta!
Esta calculadora vai ajudar você a entender a quantidade de CO2 que você gera por mês
e fornecer equivalências para ações sustentáveis.
""")

st.header("1. Energia e Eletricidade")
eletricidade = st.number_input("Consumo mensal de eletricidade (kWh):", min_value=0.0, step=1.0)
emissao_eletricidade = eletricidade * 0.5  # Média de emissão por kWh (em kg de CO2)

energia_solar = st.checkbox("Utiliza energia solar?")
if energia_solar:
    emissao_eletricidade *= 0.2  # Redução de emissões se utilizar energia solar

energia_eolica = st.checkbox("Utiliza energia eólica?")
if energia_eolica:
    emissao_eletricidade *= 0.1  # Redução maior de emissões se utilizar energia eólica

st.header("2. Transporte")
km_carro = st.number_input("Quilômetros percorridos de carro por mês:", min_value=0.0, step=1.0)
tipo_combustivel = st.selectbox("Tipo de combustível:", ["Gasolina", "Diesel", "Álcool"])

if tipo_combustivel == "Gasolina":
    emissao_carro = km_carro * 0.2  # Emissão média para gasolina (em kg de CO2 por km)
elif tipo_combustivel == "Diesel":
    emissao_carro = km_carro * 0.27  # Emissão média para diesel
else:
    emissao_carro = km_carro * 0.1  # Emissão média para álcool

st.header("3. Resíduos")
quantidade_residuos = st.number_input("Quantidade de resíduos produzidos por semana (kg):", min_value=0.0, step=1.0)
emissao_residuos = quantidade_residuos * 4 * 0.1  # Aproximação para CO2 por kg de resíduo em um mês

st.header("4. Alimentação")
dieta = st.selectbox("Qual o seu tipo de dieta?", ["Onívora", "Vegetariana", "Vegana"])

if dieta == "Onívora":
    emissao_alimentacao = 300  # Aproximação de emissão mensal em kg de CO2
elif dieta == "Vegetariana":
    emissao_alimentacao = 200
else:
    emissao_alimentacao = 150

emissao_total = emissao_eletricidade + emissao_carro + emissao_residuos + emissao_alimentacao

# Equivalências
equivalencia_arvores = calcular_equivalencia_arvores(emissao_total)
equivalencia_carros = calcular_equivalencia_carros(emissao_total)

# Relatório visual
st.markdown("""
## :bar_chart: Resultados
""")
st.write(f"**Emissões de eletricidade:** {emissao_eletricidade:.2f} kg CO2 por mês")
st.write(f"**Emissões de transporte:** {emissao_carro:.2f} kg CO2 por mês")
st.write(f"**Emissões de resíduos:** {emissao_residuos:.2f} kg CO2 por mês")
st.write(f"**Emissões de alimentação:** {emissao_alimentacao:.2f} kg CO2 por mês")
st.markdown(f"### :sparkles: **Emissão total estimada:** {emissao_total:.2f} kg CO2 por mês")

# Adicionando equivalências de sustentabilidade
st.markdown("---")
st.markdown("## :seedling: Ações de sustentabilidade equivalentes")
st.write(f":deciduous_tree: **Número de árvores necessárias para absorver essa quantidade de CO2 em um ano:** {math.ceil(equivalencia_arvores):,} árvores")
st.write(f":car: **Equivalente ao impacto de {equivalencia_carros:.2f} carros por ano**")

st.markdown("---")
st.markdown("### :bulb: **Dicas para reduzir sua pegada de carbono:**")
st.markdown("""
- Reduza o consumo de eletricidade desligando aparelhos que não estão em uso.
- Use meios de transporte mais sustentáveis, como bicicleta ou transporte público.
- Tente diminuir o desperdício de alimentos e aumente a reciclagem.
- Considere adotar uma dieta mais baseada em vegetais.
""")

# Elementos visuais adicionais
st.markdown("---")
st.markdown("### :dart: **Progresso em relação ao impacto do CO2**")
st.progress(emissao_total / 1000, text=f"Emissão Total: {emissao_total:.2f} kg CO2")  # Barra de progresso mais espessa e com valor exibido


st.write("---")
st.markdown("### Limitações e Avisos")
st.caption("⚠️ Essa calcadora é um protótipo educacional com estimativas simplificadas. Para inventários oficiais, siga GHG Protocol e ISO 14064/14067 e outras fontes.")
