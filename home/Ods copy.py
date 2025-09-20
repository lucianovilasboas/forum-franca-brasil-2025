import streamlit as st

# Dicionário com todos os 17 ODS, suas descrições, detalhes, emojis e links
ods_dict = {
    "1 - Erradicação da Pobreza": {
        "emoji": "🌍",
        "descricao": "Acabar com a pobreza em todas as suas formas, em todos os lugares.",
        "detalhes": "A erradicação da pobreza envolve garantir o acesso igualitário a recursos econômicos, bem como a serviços básicos, tecnologia e proteção social.",
        "link": "https://www.un.org/sustainabledevelopment/poverty/"
    },
    "2 - Fome Zero e Agricultura Sustentável": {
        "emoji": "🌾",
        "descricao": "Acabar com a fome, alcançar a segurança alimentar e melhoria da nutrição, e promover a agricultura sustentável.",
        "detalhes": "Este objetivo promove práticas agrícolas resilientes, investimento em infraestrutura rural e suporte aos pequenos agricultores.",
        "link": "https://www.un.org/sustainabledevelopment/hunger/"
    },
    "3 - Saúde e Bem-Estar": {
        "emoji": "💊",
        "descricao": "Garantir o acesso à saúde de qualidade e promover o bem-estar para todos, em todas as idades.",
        "detalhes": "Envolve o combate a doenças epidêmicas, acesso universal a serviços de saúde e promoção de saúde mental e bem-estar.",
        "link": "https://www.un.org/sustainabledevelopment/health/"
    },
    "4 - Educação de Qualidade": {
        "emoji": "📚",
        "descricao": "Assegurar a educação inclusiva, equitativa e de qualidade e promover oportunidades de aprendizado ao longo da vida.",
        "detalhes": "Este objetivo visa eliminar disparidades no acesso à educação e garantir oportunidades iguais para todos.",
        "link": "https://www.un.org/sustainabledevelopment/education/"
    },
    "5 - Igualdade de Gênero": {
        "emoji": "⚖️",
        "descricao": "Alcançar a igualdade de gênero e empoderar todas as mulheres e meninas.",
        "detalhes": "Visa eliminar todas as formas de discriminação e violência contra mulheres e meninas, promovendo igualdade em todas as esferas da vida.",
        "link": "https://www.un.org/sustainabledevelopment/gender-equality/"
    },
    "6 - Água Potável e Saneamento": {
        "emoji": "💧",
        "descricao": "Garantir disponibilidade e manejo sustentável da água e saneamento para todos.",
        "detalhes": "Este objetivo trata de proteger os recursos hídricos, ampliar o acesso a água limpa e saneamento adequado.",
        "link": "https://www.un.org/sustainabledevelopment/water-and-sanitation/"
    },
    "7 - Energia Limpa e Acessível": {
        "emoji": "⚡",
        "descricao": "Garantir acesso à energia barata, confiável, sustentável e renovável para todos.",
        "detalhes": "Busca promover energia limpa e aumentar a eficiência energética em todos os setores.",
        "link": "https://www.un.org/sustainabledevelopment/energy/"
    },
    "8 - Trabalho Decente e Crescimento Econômico": {
        "emoji": "💼",
        "descricao": "Promover o crescimento econômico sustentado, inclusivo e sustentável, emprego pleno e produtivo, e trabalho decente para todos.",
        "detalhes": "Foca na redução do desemprego, especialmente entre os jovens, e na erradicação de formas de trabalho forçado.",
        "link": "https://www.un.org/sustainabledevelopment/economic-growth/"
    },
    "9 - Indústria, Inovação e Infraestrutura": {
        "emoji": "🏗️",
        "descricao": "Construir infraestrutura resiliente, promover a industrialização inclusiva e sustentável, e fomentar a inovação.",
        "detalhes": "Incentiva investimentos em infraestrutura sustentável e apoio à pesquisa e inovação tecnológica.",
        "link": "https://www.un.org/sustainabledevelopment/infrastructure-industrialization/"
    },
    "10 - Redução das Desigualdades": {
        "emoji": "🤝",
        "descricao": "Reduzir as desigualdades dentro dos países e entre eles.",
        "detalhes": "Este objetivo busca empoderar populações marginalizadas e reduzir as desigualdades de renda e oportunidades.",
        "link": "https://www.un.org/sustainabledevelopment/inequality/"
    },
    "11 - Cidades e Comunidades Sustentáveis": {
        "emoji": "🏙️",
        "descricao": "Tornar as cidades e comunidades inclusivas, seguras, resilientes e sustentáveis.",
        "detalhes": "Foca no planejamento urbano sustentável e na redução de impactos ambientais em áreas urbanas.",
        "link": "https://www.un.org/sustainabledevelopment/cities/"
    },
    "12 - Consumo e Produção Responsáveis": {
        "emoji": "♻️",
        "descricao": "Garantir padrões de consumo e produção sustentáveis.",
        "detalhes": "Promove práticas de reciclagem, eficiência no uso de recursos e redução do desperdício.",
        "link": "https://www.un.org/sustainabledevelopment/sustainable-consumption-production/"
    },
    "13 - Ação Contra a Mudança Global do Clima": {
        "emoji": "🌍",
        "descricao": "Tomar medidas urgentes para combater a mudança climática e seus impactos.",
        "detalhes": "Este objetivo promove ações para mitigar os efeitos das mudanças climáticas e adaptar-se a seus impactos.",
        "link": "https://www.un.org/sustainabledevelopment/climate-change/"
    },
    "14 - Vida na Água": {
        "emoji": "🐠",
        "descricao": "Conservar e usar de forma sustentável os oceanos, mares e recursos marinhos.",
        "detalhes": "Visa proteger a biodiversidade marinha e combater a poluição nos oceanos.",
        "link": "https://www.un.org/sustainabledevelopment/oceans/"
    },
    "15 - Vida Terrestre": {
        "emoji": "🌳",
        "descricao": "Proteger, restaurar e promover o uso sustentável dos ecossistemas terrestres.",
        "detalhes": "Inclui o combate à desertificação, proteção da biodiversidade e florestas.",
        "link": "https://www.un.org/sustainabledevelopment/biodiversity/"
    },
    "16 - Paz, Justiça e Instituições Eficazes": {
        "emoji": "🕊️",
        "descricao": "Promover sociedades pacíficas e inclusivas para o desenvolvimento sustentável.",
        "detalhes": "Foca em reduzir todas as formas de violência, promover o acesso à justiça e construir instituições eficazes.",
        "link": "https://www.un.org/sustainabledevelopment/peace-justice/"
    },
    "17 - Parcerias e Meios de Implementação": {
        "emoji": "🤝",
        "descricao": "Fortalecer os meios de implementação e revitalizar a parceria global para o desenvolvimento sustentável.",
        "detalhes": "Enfatiza a importância da cooperação internacional, do comércio justo e do acesso à tecnologia para alcançar os objetivos.",
        "link": "https://www.un.org/sustainabledevelopment/globalpartnerships/"
    }
}

# Título da página
st.title("🌟 Objetivos de Desenvolvimento Sustentável (ODS) 🌟")

# Subtítulo
st.subheader("Conheça os 17 Objetivos da ONU para transformar o mundo até 2030!")

# Introdução
st.markdown("""
Os Objetivos de Desenvolvimento Sustentável (ODS) são uma agenda universal para um futuro melhor. Abaixo, explore cada objetivo e descubra como podemos construir juntos um mundo mais justo, inclusivo e sustentável.
""")

# Exibição dos 17 ODS
for ods, conteudo in ods_dict.items():
    st.markdown(f"## {conteudo['emoji']} {ods}")
    st.markdown(f"**Descrição:** {conteudo['descricao']}")
    st.markdown(f"**Detalhes:** {conteudo['detalhes']}")
    st.markdown(f"[🔗 Saiba mais sobre este ODS]({conteudo['link']})")  # Link oficial
    st.divider()  # Linha divisória entre os ODS

