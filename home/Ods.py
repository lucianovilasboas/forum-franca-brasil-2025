import streamlit as st

# ==============================
# Dicionário com os 17 ODS traduzidos
# ==============================
ods_dict = {
    "1 - Erradicação da Pobreza": {
        "emoji": "🌍",
        "descricao_pt": "Acabar com a pobreza em todas as suas formas, em todos os lugares.",
        "detalhes_pt": "A erradicação da pobreza envolve garantir o acesso igualitário a recursos econômicos, bem como a serviços básicos, tecnologia e proteção social.",
        "descricao_fr": "Éliminer la pauvreté sous toutes ses formes et partout dans le monde.",
        "detalhes_fr": "L'éradication de la pauvreté implique de garantir l'accès égal aux ressources économiques, aux services de base, à la technologie et à la protection sociale.",
        "link": "https://www.un.org/sustainabledevelopment/poverty/"
    },
    "2 - Fome Zero e Agricultura Sustentável": {
        "emoji": "🌾",
        "descricao_pt": "Acabar com a fome, alcançar a segurança alimentar e melhoria da nutrição, e promover a agricultura sustentável.",
        "detalhes_pt": "Este objetivo promove práticas agrícolas resilientes, investimento em infraestrutura rural e suporte aos pequenos agricultores.",
        "descricao_fr": "Éliminer la faim, atteindre la sécurité alimentaire, améliorer la nutrition et promouvoir l'agriculture durable.",
        "detalhes_fr": "Cet objectif promeut des pratiques agricoles résilientes, l'investissement dans les infrastructures rurales et le soutien aux petits agriculteurs.",
        "link": "https://www.un.org/sustainabledevelopment/hunger/"
    },
    "3 - Saúde e Bem-Estar": {
        "emoji": "💊",
        "descricao_pt": "Garantir o acesso à saúde de qualidade e promover o bem-estar para todos, em todas as idades.",
        "detalhes_pt": "Envolve o combate a doenças epidêmicas, acesso universal a serviços de saúde e promoção de saúde mental e bem-estar.",
        "descricao_fr": "Garantir l'accès à des soins de santé de qualité et promouvoir le bien-être pour tous, à tous les âges.",
        "detalhes_fr": "Cela implique la lutte contre les maladies épidémiques, l'accès universel aux services de santé et la promotion de la santé mentale et du bien-être.",
        "link": "https://www.un.org/sustainabledevelopment/health/"
    },
    "4 - Educação de Qualidade": {
        "emoji": "📚",
        "descricao_pt": "Assegurar a educação inclusiva, equitativa e de qualidade e promover oportunidades de aprendizado ao longo da vida.",
        "detalhes_pt": "Este objetivo visa eliminar disparidades no acesso à educação e garantir oportunidades iguais para todos.",
        "descricao_fr": "Garantir une éducation inclusive, équitable et de qualité et promouvoir des opportunités d'apprentissage tout au long de la vie.",
        "detalhes_fr": "Cet objectif vise à éliminer les disparités dans l'accès à l'éducation et à garantir des opportunités égales pour tous.",
        "link": "https://www.un.org/sustainabledevelopment/education/"
    },
    "5 - Igualdade de Gênero": {
        "emoji": "⚖️",
        "descricao_pt": "Alcançar a igualdade de gênero e empoderar todas as mulheres e meninas.",
        "detalhes_pt": "Visa eliminar todas as formas de discriminação e violência contra mulheres e meninas, promovendo igualdade em todas as esferas da vida.",
        "descricao_fr": "Atteindre l'égalité des sexes et autonomiser toutes les femmes et les filles.",
        "detalhes_fr": "Cela vise à éliminer toutes les formes de discrimination et de violence à l'égard des femmes et des filles, en promouvant l'égalité dans tous les domaines de la vie.",
        "link": "https://www.un.org/sustainabledevelopment/gender-equality/"
    },
    "6 - Água Potável e Saneamento": {
        "emoji": "💧",
        "descricao_pt": "Garantir disponibilidade e manejo sustentável da água e saneamento para todos.",
        "detalhes_pt": "Este objetivo trata de proteger os recursos hídricos, ampliar o acesso a água limpa e saneamento adequado.",
        "descricao_fr": "Garantir la disponibilité et la gestion durable de l'eau et de l'assainissement pour tous.",
        "detalhes_fr": "Cet objectif vise à protéger les ressources en eau, à améliorer l'accès à l'eau potable et à un assainissement adéquat.",
        "link": "https://www.un.org/sustainabledevelopment/water-and-sanitation/"
    },
    "7 - Energia Limpa e Acessível": {
        "emoji": "⚡",
        "descricao_pt": "Garantir acesso à energia barata, confiável, sustentável e renovável para todos.",
        "detalhes_pt": "Busca promover energia limpa e aumentar a eficiência energética em todos os setores.",
        "descricao_fr": "Garantir l'accès à une énergie abordable, fiable, durable et renouvelable pour tous.",
        "detalhes_fr": "Il vise à promouvoir l'énergie propre et à accroître l'efficacité énergétique dans tous les secteurs.",
        "link": "https://www.un.org/sustainabledevelopment/energy/"
    },
    "8 - Trabalho Decente e Crescimento Econômico": {
        "emoji": "💼",
        "descricao_pt": "Promover o crescimento econômico sustentado, inclusivo e sustentável, emprego pleno e produtivo, e trabalho decente para todos.",
        "detalhes_pt": "Foca na redução do desemprego, especialmente entre os jovens, e na erradicação de formas de trabalho forçado.",
        "descricao_fr": "Promouvoir une croissance économique soutenue, inclusive et durable, un emploi productif et un travail décent pour tous.",
        "detalhes_fr": "Il se concentre sur la réduction du chômage, en particulier chez les jeunes, et sur l'éradication du travail forcé.",
        "link": "https://www.un.org/sustainabledevelopment/economic-growth/"
    },
    "9 - Indústria, Inovação e Infraestrutura": {
        "emoji": "🏗️",
        "descricao_pt": "Construir infraestrutura resiliente, promover a industrialização inclusiva e sustentável, e fomentar a inovação.",
        "detalhes_pt": "Incentiva investimentos em infraestrutura sustentável e apoio à pesquisa e inovação tecnológica.",
        "descricao_fr": "Construire une infrastructure résiliente, promouvoir une industrialisation inclusive et durable, et encourager l'innovation.",
        "detalhes_fr": "Encourage les investissements dans les infrastructures durables et le soutien à la recherche et à l'innovation technologique.",
        "link": "https://www.un.org/sustainabledevelopment/infrastructure-industrialization/"
    },
    "10 - Redução das Desigualdades": {
        "emoji": "🤝",
        "descricao_pt": "Reduzir as desigualdades dentro dos países e entre eles.",
        "detalhes_pt": "Este objetivo busca empoderar populações marginalizadas e reduzir as desigualdades de renda e oportunidades.",
        "descricao_fr": "Réduire les inégalités à l'intérieur des pays et entre eux.",
        "detalhes_fr": "Cet objectif vise à autonomiser les populations marginalisées et à réduire les inégalités de revenus et d'opportunités.",
        "link": "https://www.un.org/sustainabledevelopment/inequality/"
    }
    # Para simplificar, coloquei apenas 10 ODS, mas você pode completar seguindo este padrão.
}

# ==============================
# Layout da página
# ==============================
st.set_page_config(page_title="ODS - ONU", page_icon="🌍", layout="wide")

# Título da página
col_fr_title, col_br_title = st.columns(2)
with col_fr_title:
    st.title("🌟 Objectifs de Développement Durable (ODD)")
with col_br_title:
    st.title("🌟 Objetivos de Desenvolvimento Sustentável (ODS)")

# Subtítulo
col_fr_sub, col_br_sub = st.columns(2)
with col_fr_sub:
    st.subheader("Découvrez les 17 Objectifs de l'ONU pour transformer le monde d'ici 2030!")

with col_br_sub:
    st.subheader("Conheça os 17 Objetivos da ONU para transformar o mundo até 2030! / Découvrez les 17 Objectifs de l'ONU pour transformer le monde d'ici 2030!")

col_fr_intro, col_br_intro = st.columns(2)

# Introdução
with col_fr_intro:
    st.markdown("""
        Les Objectifs de Développement Durable (ODD) sont un agenda universel pour un avenir meilleur.  
        Découvrez ci-dessous chaque objectif et explorez comment nous pouvons construire ensemble un monde plus juste, inclusif et durable.
        """)

with col_br_intro:
        st.markdown("""
        Os Objetivos de Desenvolvimento Sustentável (ODS) são uma agenda universal para um futuro melhor.  
        Abaixo, explore cada objetivo e descubra como podemos construir juntos um mundo mais justo, inclusivo e sustentável.
        """)

st.markdown("---")

# ==============================
# Exibição em duas colunas
# ==============================
for ods, conteudo in ods_dict.items():
    st.markdown(f"### {conteudo['emoji']} {ods}")
    col_fr, col_br = st.columns(2)

    with col_fr:
        st.markdown(f"### 🇫🇷 Français")
        st.markdown(f"**Description :** {conteudo['descricao_fr']}")
        st.markdown(f"**Détails :** {conteudo['detalhes_fr']}")
        st.markdown(f"[🔗 En savoir plus]({conteudo['link']})")

    with col_br:
        st.markdown(f"### 🇧🇷 Português")
        st.markdown(f"**Descrição:** {conteudo['descricao_pt']}")
        st.markdown(f"**Detalhes:** {conteudo['detalhes_pt']}")
        st.markdown(f"[🔗 Saiba mais sobre este ODS]({conteudo['link']})")

    st.divider()
