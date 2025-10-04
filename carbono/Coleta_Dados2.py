import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="🌳 Carbono Estocado em Florestas", page_icon="🌿", layout="wide")

st.title("🌳 Cálculo e Análise do Carbono Estocado em Florestas")
st.info("Este painel mostra os dados e cálculos relacionados ao carbono estocado em florestas, com base em medições de DAP (Diâmetro à Altura do Peito) para árvores vivas, mortas em pé e mortas caídas.")
        

# =====================
# Dados brutos (EMBUTIDOS)
# =====================
st.markdown("## 📄 Dados coletados (embutidos no código)")

data_vivas = [
    {'DAP arvores vivas': 3.0, 'Quantidade de matéria vegetal': 16.11078769},
    {'DAP arvores vivas': 3.0, 'Quantidade de matéria vegetal': 16.11078769},
    {'DAP arvores vivas': 3.8, 'Quantidade de matéria vegetal': 29.29897987},
    {'DAP arvores vivas': 5.6, 'Quantidade de matéria vegetal': 78.14761141},
    {'DAP arvores vivas': 5.7, 'Quantidade de matéria vegetal': 81.72659118},
    {'DAP arvores vivas': 5.8, 'Quantidade de matéria vegetal': 85.40294042},
    {'DAP arvores vivas': 7.0, 'Quantidade de matéria vegetal': 137.4352198},
    {'DAP arvores vivas': 7.5, 'Quantidade de matéria vegetal': 163.6458501},
    {'DAP arvores vivas': 9.0, 'Quantidade de matéria vegetal': 259.5574799},
    {'DAP arvores vivas': 9.0, 'Quantidade de matéria vegetal': 259.5574799},
    {'DAP arvores vivas': 9.0, 'Quantidade de matéria vegetal': 259.5574799},
    {'DAP arvores vivas': 10.0, 'Quantidade de matéria vegetal': 338.8441561},
    {'DAP arvores vivas': 10.0, 'Quantidade de matéria vegetal': 338.8441561},
    {'DAP arvores vivas': 10.0, 'Quantidade de matéria vegetal': 338.8441561},
    {'DAP arvores vivas': 10.0, 'Quantidade de matéria vegetal': 338.8441561},
    {'DAP arvores vivas': 11.0, 'Quantidade de matéria vegetal': 431.2444248},
    {'DAP arvores vivas': 11.0, 'Quantidade de matéria vegetal': 431.2444248},
    {'DAP arvores vivas': 13.0, 'Quantidade de matéria vegetal': 658.0769530},
    {'DAP arvores vivas': 13.0, 'Quantidade de matéria vegetal': 658.0769530},
    {'DAP arvores vivas': 13.0, 'Quantidade de matéria vegetal': 658.0769530},
    {'DAP arvores vivas': 13.8, 'Quantidade de matéria vegetal': 765.4099236},
    {'DAP arvores vivas': 14.0, 'Quantidade de matéria vegetal': 793.7869052},
    {'DAP arvores vivas': 14.0, 'Quantidade de matéria vegetal': 793.7869052},
    {'DAP arvores vivas': 14.0, 'Quantidade de matéria vegetal': 793.7869052},
    {'DAP arvores vivas': 15.7, 'Quantidade de matéria vegetal': 1060.781948},
    {'DAP arvores vivas': 15.8, 'Quantidade de matéria vegetal': 1077.959465},
    {'DAP arvores vivas': 16.0, 'Quantidade de matéria vegetal': 1112.816499},
    {'DAP arvores vivas': 17.0, 'Quantidade de matéria vegetal': 1297.286119},
    {'DAP arvores vivas': 18.0, 'Quantidade de matéria vegetal': 1499.130493},
    {'DAP arvores vivas': 18.0, 'Quantidade de matéria vegetal': 1499.130493},
    {'DAP arvores vivas': 18.0, 'Quantidade de matéria vegetal': 1499.130493},
    {'DAP arvores vivas': 19.0, 'Quantidade de matéria vegetal': 1718.884164},
    {'DAP arvores vivas': 19.0, 'Quantidade de matéria vegetal': 1718.884164},
    {'DAP arvores vivas': 20.0, 'Quantidade de matéria vegetal': 1957.067879},
    {'DAP arvores vivas': 23.0, 'Quantidade de matéria vegetal': 2787.221126},
    {'DAP arvores vivas': 24.0, 'Quantidade de matéria vegetal': 3104.090978},
    {'DAP arvores vivas': 26.0, 'Quantidade de matéria vegetal': 3800.866102},
    {'DAP arvores vivas': 26.0, 'Quantidade de matéria vegetal': 3800.866102},
    {'DAP arvores vivas': 26.0, 'Quantidade de matéria vegetal': 3800.866102},
    {'DAP arvores vivas': 26.0, 'Quantidade de matéria vegetal': 3800.866102},
    {'DAP arvores vivas': 27.0, 'Quantidade de matéria vegetal': 4181.675452},
    {'DAP arvores vivas': 27.0, 'Quantidade de matéria vegetal': 4181.675452},
    {'DAP arvores vivas': 28.0, 'Quantidade de matéria vegetal': 4584.68835},
    {'DAP arvores vivas': 28.0, 'Quantidade de matéria vegetal': 4584.68835},
    {'DAP arvores vivas': 29.0, 'Quantidade de matéria vegetal': 5010.336963},
    {'DAP arvores vivas': 32.0, 'Quantidade de matéria vegetal': 6427.31293},
    {'DAP arvores vivas': 32.0, 'Quantidade de matéria vegetal': 6427.31293},
    {'DAP arvores vivas': 33.0, 'Quantidade de matéria vegetal': 6947.687369},
    {'DAP arvores vivas': 33.0, 'Quantidade de matéria vegetal': 6947.687369},
    {'DAP arvores vivas': 40.0, 'Quantidade de matéria vegetal': 11303.46979},
    {'DAP arvores vivas': 47.0, 'Quantidade de matéria vegetal': 16998.38183},
    {'DAP arvores vivas': 72.7, 'Quantidade de matéria vegetal': 51248.60632}
]


data_mortas_pe = [
    {'DAP mortas em pé': 9.0, 'Quantidade de matéria vegetal': 259.5574799},
    {'DAP mortas em pé': 13.0, 'Quantidade de matéria vegetal': 658.0769530},
    {'DAP mortas em pé': 14.0, 'Quantidade de matéria vegetal': 793.7869052},
    {'DAP mortas em pé': 15.0, 'Quantidade de matéria vegetal': 945.1720825},
    {'DAP mortas em pé': 16.0, 'Quantidade de matéria vegetal': 1112.8164990},
    {'DAP mortas em pé': 17.0, 'Quantidade de matéria vegetal': 1297.2861190},
    {'DAP mortas em pé': 18.0, 'Quantidade de matéria vegetal': 1499.1304930},
    {'DAP mortas em pé': 18.0, 'Quantidade de matéria vegetal': 1499.1304930},
    {'DAP mortas em pé': 19.0, 'Quantidade de matéria vegetal': 1718.8841640},
    {'DAP mortas em pé': 20.0, 'Quantidade de matéria vegetal': 1957.0678790},
    {'DAP mortas em pé': 20.0, 'Quantidade de matéria vegetal': 1957.0678790},
    {'DAP mortas em pé': 25.0, 'Quantidade de matéria vegetal': 3441.8205390},
    {'DAP mortas em pé': 70.0, 'Quantidade de matéria vegetal': 46569.12107}
]


data_mortas_caidas = [
    {'DAP': 10.0, 'L': 1.3, 'DAP2': 100.0, 'DAP2xL': 130.0},
    {'DAP': 18.0, 'L': 1.7, 'DAP2': 324.0, 'DAP2xL': 550.8},
    {'DAP': 28.0, 'L': 8.5, 'DAP2': 784.0, 'DAP2xL': 6664.0},
    {'DAP': 26.0, 'L': 2.8, 'DAP2': 676.0, 'DAP2xL': 1892.8},
    {'DAP': 26.0, 'L': 1.7, 'DAP2': 676.0, 'DAP2xL': 1149.2},
    {'DAP': 14.0, 'L': 3.0, 'DAP2': 196.0, 'DAP2xL': 588.0}
]

df_vivas = pd.DataFrame(data_vivas)
df_mortas_pe = pd.DataFrame(data_mortas_pe)
df_mortas_caidas = pd.DataFrame(data_mortas_caidas)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("### 🌱 DAP — Árvores Vivas")
    st.dataframe(df_vivas, use_container_width=True, height=320)
with col_b:
    st.markdown("### 🌲 DAP — Mortas em Pé")
    st.dataframe(df_mortas_pe, use_container_width=True, height=320)

st.markdown("### 🌿 DAP — Mortas Caídas")
st.dataframe(df_mortas_caidas, use_container_width=True)


# =====================
# Explicação dos Cálculos (com fórmulas em LaTeX)
# =====================
st.markdown("## 🧮 Como são feitos os cálculos")

st.markdown("""
A partir da folha **Carbono_Estocado**, inferimos a fração média de carbono na matéria vegetal como **0.45** (≈45%), 
valor compatível com referências técnicas (entre 0,45 e 0,50).  
Os cálculos seguem as seguintes etapas:
""")

# 1) Biomassa -> Carbono
st.markdown("### 1️⃣ Conversão de Biomassa em Carbono (tC)")
st.latex(r"""
C = B \times f_C
""")
st.markdown("""
onde:  
- \( C \) = quantidade de **carbono estocado** (tC);  
- \( B \) = **biomassa total** (t);  
- \( f_C \) = **fração média de carbono na biomassa**, adotada como 0,45.
""")

# 2) Carbono -> CO2 Equivalente
st.markdown("### 2️⃣ Conversão de Carbono em Dióxido de Carbono Equivalente (tCO₂e)")
st.latex(r"""
CO_{2e} = C \times \frac{44}{12}
""")
st.markdown("""
O fator estequiométrico \\( \\tfrac{44}{12} \\approx 3{,}67 \\) decorre da relação entre as massas molares 
do dióxido de carbono (CO₂) e do carbono (C):  
- Massa molar do CO₂ = 44 g/mol  
- Massa molar do C = 12 g/mol  
""")

# 3) Carbono por hectare
st.markdown("### 3️⃣ Carbono por Unidade de Área (tC/ha)")
st.latex(r"""
C_{ha} = \frac{C}{A}
""")
st.markdown("""
onde:  
- \( C_{ha} \) = **carbono por hectare** (tC/ha);  
- \( A \) = **área amostrada** (ha).  
""")

# Observações adicionais
st.markdown("""
### 📘 Observações Importantes

- **DAP_Vivas** e **DAP_Mortas_Em_Pe**: possuem as colunas *DAP* e **Quantidade de matéria vegetal** (considerada a biomassa individual).  
- **DAP_Mortas_Caidas**: contém *DAP*, *L*, *DAP²* e *DAP² × L*, que representam um **índice volumétrico** aproximado.  
  Como não há dados de densidade ou fatores alométricos específicos, a conversão para toneladas é substituída por métricas **relativas**, 
  evitando super ou subestimativas.
""")


# =====================
# Totais consolidados (da planilha)
# =====================
FATOR_CO2E = 44/12
TOTAL_MATERIA_VEG = 247788.508069
TOTAL_CARBONO_T = 111504.828631

col1, col2, col3 = st.columns(3)
col1.metric("Matéria vegetal total (unid. da planilha)", f"{TOTAL_MATERIA_VEG:,.2f}")
col2.metric("Carbono total (tC)", f"{TOTAL_CARBONO_T:,.2f}")
col3.metric("CO₂e total (tCO₂e)", f"{(TOTAL_CARBONO_T*FATOR_CO2E):,.2f}")

st.info("A fração de carbono inferida da planilha é ≈ **45.00%** (Carbono/Massa).")

# =====================
# Cálculos automáticos por registro (quando aplicável)
# =====================
F_C = 0.45  # fração de carbono inferida (≈0,45)
if "Quantidade de matéria vegetal" in df_vivas.columns:
    df_vivas["Carbono estimado (tC)"] = df_vivas["Quantidade de matéria vegetal"] * F_C
    df_vivas["CO₂e estimado (tCO₂e)"] = df_vivas["Carbono estimado (tC)"] * FATOR_CO2E

if "Quantidade de matéria vegetal" in df_mortas_pe.columns:
    df_mortas_pe["Carbono estimado (tC)"] = df_mortas_pe["Quantidade de matéria vegetal"] * F_C
    df_mortas_pe["CO₂e estimado (tCO₂e)"] = df_mortas_pe["Carbono estimado (tC)"] * FATOR_CO2E

st.markdown("### 📊 Tabelas com estimativas (quando aplicável)")
colx, coly = st.columns(2)
with colx:
    if "Carbono estimado (tC)" in df_vivas.columns:
        st.markdown("**Árvores Vivas — com estimativas**")
        st.dataframe(df_vivas, use_container_width=True, height=320)
with coly:
    if "Carbono estimado (tC)" in df_mortas_pe.columns:
        st.markdown("**Mortas em Pé — com estimativas**")
        st.dataframe(df_mortas_pe, use_container_width=True, height=320)

# =====================
# Visualizações
# =====================
st.markdown("## 🌍 Visualizações")

# Distribuições de DAP
c1, c2, c3 = st.columns(3)
with c1:
    if "DAP arvores vivas" in df_vivas.columns:
        fig = px.histogram(df_vivas, x="DAP arvores vivas", nbins=15, title="Distribuição de DAP — Árvores Vivas")
        st.plotly_chart(fig, use_container_width=True)
with c2:
    if "DAP mortas em pé" in df_mortas_pe.columns:
        fig = px.histogram(df_mortas_pe, x="DAP mortas em pé", nbins=10, title="Distribuição de DAP — Mortas em Pé")
        st.plotly_chart(fig, use_container_width=True)
with c3:
    if "DAP2xL" in df_mortas_caidas.columns:
        fig = px.histogram(df_mortas_caidas, x="DAP2xL", nbins=10, title="Distribuição de DAP2xL — Mortas Caídas")
        st.plotly_chart(fig, use_container_width=True)

# Barras de biomassa (vivas e mortas em pé)
if "Quantidade de matéria vegetal" in df_vivas.columns and "Quantidade de matéria vegetal" in df_mortas_pe.columns:
    soma_vivas = df_vivas["Quantidade de matéria vegetal"].sum()
    soma_mortas_pe = df_mortas_pe["Quantidade de matéria vegetal"].sum()
    df_bar = pd.DataFrame({
        "Categoria": ["Árvores Vivas", "Mortas em Pé"],
        "Matéria vegetal (soma)": [soma_vivas, soma_mortas_pe]
    })
    fig_bar = px.bar(df_bar, x="Categoria", y="Matéria vegetal (soma)", text_auto=".2f",
                     title="Soma da Matéria Vegetal — Vivas vs Mortas em Pé")
    st.plotly_chart(fig_bar, use_container_width=True)

# Treemap/Índice para mortas caídas com DAP2xL
if "DAP2xL" in df_mortas_caidas.columns:
    df_mc = df_mortas_caidas.copy()
    df_mc["Índice (DAP2xL normalizado)"] = df_mc["DAP2xL"] / df_mc["DAP2xL"].sum()
    fig_treemap = px.treemap(df_mc, path=["DAP"], values="DAP2xL",
                             title="Contribuição relativa por peça (DAP2xL) — Mortas Caídas")
    st.plotly_chart(fig_treemap, use_container_width=True)

st.markdown("""
---
### 🧭 Conclusão
Os dados embutidos permitem **reprodutibilidade** e **transparência**: qualquer leitor pode entender as premissas e replicar os cálculos.  
Utilizamos **fração de carbono ≈ 0,45** (inferida da própria planilha) e o fator **44/12** para CO₂e.  
Para o material **morto caído**, sem parâmetros adicionais (densidade/álgebra alométrica), apresentamos **métricas relativas** (*DAP2xL*) para evitar vieses.
""")

st.caption("🌿 IFMG Campus Ponte Nova — Página gerada automaticamente a partir dos dados fornecidos.")
