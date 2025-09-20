import streamlit as st
from datetime import datetime
from openai import OpenAI 

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

# ===================================
# Cabeçalho
# ===================================
st.title("🤖 Assistente Virtual - Pegada de Carbono")
st.subheader("Converse com o assistente e tire suas dúvidas sobre sustentabilidade, cálculos e fontes atualizadas!")

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
        {"role": "system", "content": "Você é o Curupira, um assistente especialista em pegada de carbono. Responda em português, seja amigável e forneça fontes atualizadas sempre que possível."},
        {"role": "assistant", "content": "Olá! 🌱 Sou seu assistente virtual sobre pegada de carbono. Como posso te ajudar hoje?"}
    ]

# ===================================
# Função para enviar mensagem ao GPT
# ===================================
def gerar_resposta(pergunta):
    """Envia a conversa para o GPT e retorna a resposta."""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",  # você pode trocar para gpt-4.1 ou gpt-4o
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
    user_input = st.text_input("Digite sua mensagem:", placeholder="Ex: Como calcular minha pegada de carbono?")
    submitted = st.form_submit_button("Enviar")

    if submitted and user_input:
        # Adiciona mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Gera resposta do GPT
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
