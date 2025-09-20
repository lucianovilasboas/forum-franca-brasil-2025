import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------
# Configuração inicial
# ----------------------------
st.set_page_config(
    page_title="Projeção de Pegada de Carbono - Fórum Ciência e Sociedade 2025",
    page_icon="🌱",
    layout="wide"
)

st.title("🌍 Projeção de Pegada de Carbono (10 anos)")
st.markdown("""
Este painel interativo permite **projetar a pegada de carbono** para os próximos 10 anos
com base em três cenários:
- **Base:** Sem mudanças nas práticas atuais.
- **Medida 1:** Cardápio sustentável (redução gradual das emissões relacionadas à alimentação).
- **Medida 2:** Conjunto de medidas — energia solar, compostagem/reciclagem e plantio de árvores.
""")

st.info("**Ano base:** 918,2 t CO₂e/ano")

# ----------------------------
# Parâmetros fixos
# ----------------------------
BASE = 918.2
portions = {
    "diet": 909.4,       # Alimentação
    "elec": 0.6,         # Eletricidade
    "waste": 2.9,        # Resíduos
    "transport": 6.4,    # Transporte
    "water": 0.01        # Água
}
years = list(range(0, 10))  # 10 anos

# ----------------------------
# Controles interativos
# ----------------------------
st.header("Ajuste as hipóteses")

cols = st.columns(4)

with cols[0]:
    dietMax = st.slider(
        "Redução máxima de emissões da alimentação (%)",
        min_value=10, max_value=40, value=30, step=1
    )

with cols[1]:
    pvAvoid = st.slider(
        "Instalação fotovoltaica - emissões evitadas (t CO₂e/ano)",
        min_value=0.0, max_value=5.0, value=0.6, step=0.1
    )

with cols[2]:
    wastePct = st.slider(
        "Redução de emissões de resíduos (%)",
        min_value=0, max_value=80, value=50, step=5
    )

with cols[3]:
    treesPerYear = st.slider(
        "Árvores plantadas por ano",
        min_value=0, max_value=200, value=50, step=5
    )



# ----------------------------
# Funções para calcular os cenários
# ----------------------------
def compute_series():
    # Base: constante
    base = [BASE for _ in years]

    # Medida 1: redução linear da dieta até ano 5
    m1 = []
    for y in years:
        frac = min(1, y/5)
        dietNow = portions["diet"] * (1 - (dietMax/100) * frac)
        total = dietNow + portions["elec"] + portions["waste"] + portions["transport"] + portions["water"]
        m1.append(total)

    # Medida 2: cortes imediatos e sequestro cumulativo de árvores
    m2 = []
    cumulativeTrees = 0
    for y in years:
        elecNow = max(0, portions["elec"] - pvAvoid)
        wasteNow = portions["waste"] * (1 - wastePct/100)
        cumulativeTrees += treesPerYear
        sequestration = cumulativeTrees * 0.022  # 22 kg CO₂ por árvore por ano
        total = portions["diet"] + elecNow + wasteNow + portions["transport"] + portions["water"] - sequestration
        m2.append(max(0, total))  # não permite valores negativos
    return base, m1, m2

base, m1, m2 = compute_series()

# ----------------------------
# DataFrame para tabela
# ----------------------------
df = pd.DataFrame({
    "Ano": [f"Ano {y}" for y in years],
    "Base (sem mudanças)": base,
    "Medida 1 - Cardápio Sustentável": m1,
    "Medida 2 - Solar + Resíduos + Árvores": m2
})

# ----------------------------
# Gráfico interativo
# ----------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=years, y=base,
    mode='lines+markers',
    name='Base (sem mudanças)',
    line=dict(color='#60a5fa', width=3)
))

fig.add_trace(go.Scatter(
    x=years, y=m1,
    mode='lines+markers',
    name='Medida 1 — Cardápio sustentável',
    line=dict(color='#34d399', width=3)
))

fig.add_trace(go.Scatter(
    x=years, y=m2,
    mode='lines+markers',
    name='Medida 2 — Solar + resíduos + árvores',
    line=dict(color='#fbbf24', width=3)
))

fig.update_layout(
    title="Projeção da Pegada de Carbono (10 anos)",
    xaxis_title="Ano",
    yaxis_title="t CO₂e/ano",
    template="plotly_dark",
    hovermode="x unified"
)

# ----------------------------
# Layout Streamlit
# ----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Resumo Numérico")
    st.dataframe(df.style.format({"Base (sem mudanças)": "{:.1f}", 
                                  "Medida 1 - Cardápio Sustentável": "{:.1f}", 
                                  "Medida 2 - Solar + Resíduos + Árvores": "{:.1f}"}))

st.markdown("---")
st.markdown("""
💡 **Metodologia simplificada**:  
- Medida 1 aplica **redução linear** na parcela da alimentação até o 5º ano.  
- Medida 2 aplica cortes imediatos em eletricidade e resíduos, além de **sequestro cumulativo** das árvores (22 kg CO₂ por árvore por ano).

> Para inventários oficiais, seguir **GHG Protocol** e **ISO 14064/14067**.
""")
