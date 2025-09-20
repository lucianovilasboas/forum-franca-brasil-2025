import streamlit as st

# Configuração da página
st.set_page_config(page_title="Fórum Ciência e Sociedade 2025", page_icon=":earth_americas:", layout="wide")

# Título principal
st.title("Fórum Ciência e Sociedade 2025")

st.write("""
O **Fórum franco-brasileiro Ciência e Sociedade** é uma iniciativa internacional que, desde 2005,
promove o diálogo entre estudantes, professores, pesquisadores e autoridades do Brasil e da França
sobre temas de relevância científica e social. 

O evento ocorre alternadamente entre os dois países e tem como objetivo **estimular o intercâmbio cultural, acadêmico e científico**.

O ano de **2025** será especialmente simbólico, pois marcará:
- A **8ª edição** do Fórum,  
- **20 anos** de sua criação,  
- E os **200 anos de relações diplomáticas** entre Brasil e França, durante o *Ano do Brasil na França e Ano da França no Brasil*.
""")

# Tema principal
st.subheader("Tema e Subtemas")
st.write("""
**Tema central:**  
*Sistemas alimentares e mudanças climáticas: desafios e perspectivas*

Essa escolha reflete os desafios globais enfrentados por ambos os países, especialmente nas áreas de produção agrícola e sustentabilidade ambiental.

**Subtemas:**
- **Tecnologias e estratégias para uma produção agrícola sustentável:**  
  Soluções técnicas e metodológicas para melhorar a produção sem comprometer o meio ambiente.
- **Gestão de recursos naturais:**  
  Estratégias para uso racional e sustentável de recursos como água, solo e adubos orgânicos.
- **Protagonismo individual e coletivo no enfrentamento das alterações climáticas:**  
  O papel da sociedade, comunidades e instituições na construção de soluções para a crise climática.
""")

# Organização
st.subheader("Organização e Instituições Envolvidas")
st.write("""
A **organização** da edição 2025 está a cargo do **Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais (IFMG)**, Brasil, com apoio de parceiros nacionais e internacionais:

- CONIF – Conselho Nacional das Instituições da Rede Federal (Brasil)
- SETEC/MEC – Secretaria de Educação Profissional e Tecnológica (Brasil)
- Ministério da Agricultura e Soberania Alimentar da França (DGER)
- Réseau Brésil de l’Enseignement Agricole
- Embaixada da França no Brasil
- Embrapa – Empresa Brasileira de Pesquisa Agropecuária
- Ministério do Desenvolvimento Agrário e Agricultura Familiar (Brasil)
- Ministério da Agricultura e Pecuária (Brasil)

A **Comissão Organizadora** inclui representantes dos campi IFMG Bambuí, Ouro Preto e Santa Luzia,
além de membros de outros Institutos Federais e voluntários.
""")

# Local
st.subheader("Local do Evento")
st.write("""
A 8ª edição será realizada no **IFMG Campus Bambuí**, localizado a cerca de 270 km de Belo Horizonte.

Bambuí é uma cidade mineira com aproximadamente **25 mil habitantes**, com economia voltada para a agropecuária.  
O Campus possui **328,76 hectares** e infraestrutura moderna, com laboratórios, auditórios, áreas experimentais e espaços culturais,
oferecendo cursos técnicos, de graduação e pós-graduação.

**Endereço:** Fazenda Varginha, Rodovia Bambuí/Medeiros - km 05, Caixa Postal 05, Bambuí - MG, CEP: 38.900-000.
""")

# Datas
st.subheader("Cronograma do Fórum")
st.write("""
- **Fase de Sensibilização:** até 11/10/2025  
  Desenvolvimento dos projetos conjuntos entre instituições brasileiras e francesas.

- **Pré-fórum:** 12 a 18/10/2025  
  Delegações francesas visitam suas instituições parceiras no Brasil.

- **Deslocamento para Bambuí:** 19/10/2025  
  Transporte organizado pela comissão, com recepção no Aeroporto de Confins.

- **Fórum no IFMG Bambuí:** 20 a 24/10/2025  
  Oficinas técnicas e artísticas, conferências, debates, apresentações culturais e visitas técnicas.

- **Retorno das delegações:** 25/10/2025  
  Com voos programados para a tarde, a partir das 15h.
""")

# Público-alvo
st.subheader("Público-Alvo")
st.write("""
O evento reunirá aproximadamente **250 participantes**, incluindo:
- Professores/formadores e estudantes (1 professor + 4 estudantes por instituição);
- Pesquisadores e palestrantes especializados em cada subtema;
- Voluntários e equipe de apoio;
- Autoridades e convidados dos ministérios e instituições envolvidas.

Atualmente, estão pré-confirmadas **18 instituições brasileiras** e **18 instituições francesas**, que trabalharão em **pares**.
""")

# Sobre Brasil e Minas
st.subheader("Sobre o Brasil e Minas Gerais")
st.write("""
**Brasil:**  
Maior país da América do Sul, com mais de 200 milhões de habitantes e grande diversidade cultural e ambiental.
É líder mundial em produção agrícola, destacando-se em soja, milho, café, carnes e frutas.
Abriga biomas importantes como Amazônia, Cerrado e Mata Atlântica.

**Minas Gerais:**  
Segundo estado mais populoso do Brasil, com cerca de 21 milhões de habitantes.  
Conhecido por sua gastronomia, belezas naturais e produção agrícola, especialmente de leite e café.
A capital, **Belo Horizonte**, é um importante centro político, econômico e cultural.
""")

# Considerações finais
st.subheader("Considerações Finais")
st.write("""
A edição 2025 será uma **oportunidade única para fortalecer os laços de cooperação** entre Brasil e França.

Mais do que um evento, o Fórum representa **formação cidadã, científica e cultural**, preparando jovens para enfrentar desafios globais relacionados à **sustentabilidade, segurança alimentar e mudanças climáticas**.
""")

# Rodapé
st.markdown("---")
st.markdown("💡 **Desenvolvido por Luciano Vilas Boas Espiridião.**")
st.markdown("[📩 Entre em contato no LinkedIn](https://www.linkedin.com/in/luciano-espiridiao/)")
