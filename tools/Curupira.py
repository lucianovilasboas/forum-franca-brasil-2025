import streamlit as st
from datetime import datetime
from openai import OpenAI
# import google.generativeai as genai
import re

# ===================================
# Configuração inicial
# ===================================
st.set_page_config(
    page_title="🤖 Assistente Virtual - Pegada de Carbono",
    page_icon="🌱",
    layout="wide"
)

# Inicializando cliente OpenAI com chave secreta
client = OpenAI(api_key=st.secrets["openai_key"])
# genai.configure(api_key=st.secrets.api["gemini_key"])


# ===================================
# Função para cálculo da pegada de carbono
# ===================================
def calcular_pegada(consumo_energia, litros_combustivel, num_pessoas):
    """
    Calcula a pegada de carbono baseada em:
    - Consumo de energia elétrica (kWh)
    - Consumo de combustível (litros)
    - Número de pessoas
    """
    fator_energia = 0.5  # kg CO2 por kWh
    fator_combustivel = 2.31  # kg CO2 por litro de gasolina
    fator_pessoa = 100  # kg CO2 por pessoa/mês (estimativa média)

    co2_energia = consumo_energia * fator_energia
    co2_combustivel = litros_combustivel * fator_combustivel
    co2_pessoas = num_pessoas * fator_pessoa

    total = co2_energia + co2_combustivel + co2_pessoas
    return round(total, 2), round(co2_energia, 2), round(co2_combustivel, 2), round(co2_pessoas, 2)

# ===================================
# Cabeçalho
# ===================================
st.title("🤖 Assistente Virtual - Pegada de Carbono")
st.subheader("Converse com o assistente, tire dúvidas, receba fontes atualizadas e faça cálculos básicos da sua pegada de carbono!")

st.markdown("""
Este assistente foi projetado para:
- 🌍 **Explicar conceitos** sobre pegada de carbono e mudanças climáticas  
- 🔗 **Fornecer links confiáveis** e notícias atualizadas sobre o tema  
- 🧮 **Auxiliar nos cálculos da sua pegada de carbono**  
- 💬 **Conversar com você** para tirar dúvidas gerais sobre sustentabilidade
""")
st.markdown("---")

# ===================================
# Histórico de conversas
# ===================================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Você é um assistente especialista em pegada de carbono. Responda em português, de forma amigável e técnica, fornecendo fontes confiáveis sempre que possível."},
        {"role": "assistant", "content": "Olá! 🌱 Sou seu assistente virtual sobre pegada de carbono. Você pode me perguntar qualquer coisa ou me passar dados para calcular sua pegada de carbono!"}
    ]

# ===================================
# Função para detectar se é um cálculo
# ===================================
def extrair_dados_para_calculo(texto):
    """
    Detecta no texto valores para consumo de energia, combustível e pessoas.
    Exemplo: "Tenho 200 kWh, 50 litros de gasolina e 4 pessoas na casa."
    """
    energia = re.search(r"(\d+)\s*kwh", texto.lower())
    combustivel = re.search(r"(\d+)\s*litros?", texto.lower())
    pessoas = re.search(r"(\d+)\s*pessoas?", texto.lower())

    return (
        int(energia.group(1)) if energia else None,
        int(combustivel.group(1)) if combustivel else None,
        int(pessoas.group(1)) if pessoas else None
    )

# ===================================
# Função para gerar resposta do GPT
# ===================================
def gerar_resposta(pergunta):
    """
    Se detectar dados numéricos, calcula a pegada.
    Caso contrário, envia a conversa ao GPT.
    """
    energia, combustivel, pessoas = extrair_dados_para_calculo(pergunta)

    # Caso tenha dados suficientes para cálculo
    if energia is not None and combustivel is not None and pessoas is not None:
        total, co2_energia, co2_combustivel, co2_pessoas = calcular_pegada(energia, combustivel, pessoas)
        return (
            f"🧮 **Cálculo da Pegada de Carbono**\n\n"
            f"- Emissões por **energia elétrica**: {co2_energia} kg CO₂\n"
            f"- Emissões por **combustível**: {co2_combustivel} kg CO₂\n"
            f"- Emissões por **número de pessoas**: {co2_pessoas} kg CO₂\n\n"
            f"**Pegada total estimada:** {total} kg CO₂/mês\n\n"
            f"_Obs.: Este cálculo é uma estimativa baseada em médias globais._"
        )

    # Caso contrário, usa GPT normalmente
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=st.session_state.messages,
            temperature=0.6,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Erro ao se comunicar com o GPT: {str(e)}"

# ===================================
# Interface do chat
# ===================================
st.subheader("💬 Converse com o assistente")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Digite sua mensagem:",
        placeholder="Ex: Tenho 200 kWh, 50 litros de gasolina e 4 pessoas na casa"
    )
    submitted = st.form_submit_button("Enviar")

    if submitted and user_input:
        # Adiciona mensagem do usuário ao histórico
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Gera resposta (GPT ou cálculo)
        resposta = gerar_resposta(user_input)

        # Adiciona resposta ao histórico
        st.session_state.messages.append({"role": "assistant", "content": resposta})

# ===================================
# Exibição do histórico
# ===================================
st.markdown("### Histórico da Conversa")
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**👤 Você:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**🤖 Assistente:** {msg['content']}")

st.markdown("---")

# ===================================
# Links úteis
# ===================================
st.subheader("🔗 Fontes e ferramentas úteis")
st.markdown("""
- [ONU - Objetivos de Desenvolvimento Sustentável](https://brasil.un.org/pt-br/sdgs)  
- [ONU - Mudanças Climáticas](https://www.un.org/climate-change)  
- [WWF - Calculadora de Pegada de Carbono](https://www.wwf.org.br/natureza_brasileira/reducao_de_impactos2/pegada_ecologica/)  
- [Global Footprint Network](https://www.footprintnetwork.org/)
""")

st.caption(f"Página gerada em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
