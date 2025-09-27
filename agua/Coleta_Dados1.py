import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------
# Configuração inicial do Streamlit
# ---------------------------------------
st.set_page_config(page_title="Fórum França-Brasil", page_icon=":earth_americas:", layout="wide")

st.title("📊 Coleta de Dados - Pluviometria e Vazão")
st.info("Este painel mostra os dados de pluviometria, vazão e volume escoado a partir dos valores fornecidos.")

# ---------------------------------------
# Dados estáticos - diretamente no código
# ---------------------------------------
dados = {
    "Meses": [
        "maio-24", "junho-24", "julho-24", "agosto-24", "setembro-24",
        "outubro-24", "novembro-24", "dezembro-24", "janeiro-25", "fevereiro-25",
        "março-25", "abril-25", "maio-25", "junho-25", "julho-25", "agosto-25"
    ],
    "Pluviometria (mm)": [
        0, 0, 0, 6.51, 0, 352.69, 221.3, 327.36, 531.17, 36.58,
        167.82, 109.68, 0, 21.42, 0, 6.73
    ],
    "Vazão (m³/s)": [
        0, 0, 0.238, 0.25, 0.227, 0.179, 0.3, 0.357, 0.511, 0.357,
        0.511, 0.365, 0.296, 0.252, 0.242, 0
    ],
    "Segundos": [
        2678400, 2592000, 2678400, 2678400, 2592000, 2678400,
        2592000, 2678400, 2678400, 2419200, 2678400, 2592000,
        2678400, 2592000, 2678400, 2592000
    ],
    "Volume escoado (m³)": [
        0, 0, 637459.2, 669600, 588384, 479433.6, 669600, 1033528.4,
        1186562.4, 837846.4, 1366662.4, 1000512, 807480, 756864,
        648172.8, 0
    ],
    "Volume escoado trapézios (m³)": [
        308448, 0, 653529.6, 63789.6, 526176, 581212.8, 844992,
        1215939.2, 1175857.6, 1062268.8, 1201262.4, 921456, 822686.4,
        692064, 324086.4, 0
    ]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# ---------------------------------------
# Exibir tabela
# ---------------------------------------
st.subheader("📄 Dados Utilizados")
st.dataframe(df)

# ---------------------------------------
# Cálculos de Totais
# ---------------------------------------
total_esc = df["Volume escoado (m³)"].sum()
total_esc_trap = df["Volume escoado trapézios (m³)"].sum()
diferenca = ((total_esc - total_esc_trap) / total_esc_trap) * 100

st.markdown(f"""
**Total escoado (m³):** {total_esc:,.0f}  
**Total escoado - trapézios (m³):** {total_esc_trap:,.0f}  
**Diferença entre métodos:** {diferenca:.2f}%
""")

# ---------------------------------------
# Gráfico interativo Plotly
# ---------------------------------------
st.subheader("🌧️ Gráfico de Pluviometria e Vazão")

fig = go.Figure()

# Barras - Pluviometria
fig.add_trace(go.Bar(
    x=df["Meses"],
    y=df["Pluviometria (mm)"],
    name="Pluviometria (mm)",
    marker_color="royalblue",
    yaxis="y1",
    hovertemplate="<b>Mês</b>: %{x}<br><b>Pluviometria</b>: %{y} mm<extra></extra>"
))

# Linha - Vazão
fig.add_trace(go.Scatter(
    x=df["Meses"],
    y=df["Vazão (m³/s)"],
    name="Vazão (m³/s)",
    mode="lines+markers",
    marker=dict(size=8, color="red"),
    line=dict(color="red", width=2),
    yaxis="y2",
    hovertemplate="<b>Mês</b>: %{x}<br><b>Vazão</b>: %{y} m³/s<extra></extra>"
))

# Configurações do layout
fig.update_layout(
    title="Pluviometria e Vazão",
    xaxis=dict(title="Meses"),
    yaxis=dict(
        title="Pluviometria (mm)",
        titlefont=dict(color="royalblue"),
        tickfont=dict(color="royalblue"),
        side="left"
    ),
    yaxis2=dict(
        title="Vazão (m³/s)",
        titlefont=dict(color="red"),
        tickfont=dict(color="red"),
        overlaying="y",
        side="right"
    ),
    legend=dict(x=0.5, y=1.1, orientation="h", xanchor="center"),
    bargap=0.3,
    template="plotly_white",
    hovermode="x unified",
    height=600
)

# Exibir gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------
# Gráfico de Volumes Escoados
# ---------------------------------------
st.subheader("💧 Comparação dos Volumes Escoados")

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=df["Meses"],
    y=df["Volume escoado (m³)"],
    name="Volume escoado (m³)",
    marker_color="green",
    hovertemplate="<b>Mês</b>: %{x}<br><b>Volume</b>: %{y:,.0f} m³<extra></extra>"
))

fig2.add_trace(go.Bar(
    x=df["Meses"],
    y=df["Volume escoado trapézios (m³)"],
    name="Volume escoado trapézios (m³)",
    marker_color="orange",
    hovertemplate="<b>Mês</b>: %{x}<br><b>Volume Trapézio</b>: %{y:,.0f} m³<extra></extra>"
))

fig2.update_layout(
    title="Comparação de Volume Escoado",
    xaxis=dict(title="Meses"),
    yaxis=dict(title="Volume (m³)"),
    template="plotly_white",
    barmode="group",
    height=600
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------
# Observações finais
# ---------------------------------------
st.markdown("""
### 📌 Observações:
- **Pluviometria**: representada por barras azuis.
- **Vazão**: representada pela linha vermelha.
- **Volumes escoados**: comparados lado a lado (método direto x trapézios).
- Os dados foram inseridos diretamente no código para garantir reprodutibilidade.
""")
