import streamlit as st
import user # Import the user.py file


# acesse a pagina se o 'role' for um 'user'
if 'logged_in' not in st.session_state or 'role' not in st.session_state or st.session_state.role != 'user':
    st.session_state.logged_in = False


def login():
    user.init_db()
    user.main()

    # if st.button("Log in"):
    #     st.session_state.logged_in = True
    #     st.rerun()

def logout():
    st.write("Clique no botão abaixo para sair do sistema.")
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state['role'] = None
        st.session_state['username'] = None
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

principal = st.Page("home/Principal.py", title="Principal", icon=":material/home:", default=True)
forum = st.Page("home/Forum.py", title="Fórum", icon=":material/dashboard:")
# home2 = st.Page("home/Forum_bkp.py", title="Fórum2", icon=":material/dashboard:", default=False)
programacao = st.Page("home/Programacao.py", title="Programação", icon=":material/calendar_month:")

ods = st.Page("home/Ods.py", title="ODS", icon="🎯")



agua_home = st.Page("agua/Ciclo_Agua.py", title="Ciclo da Agua", icon="💧")
agua_equipes = st.Page("agua/Equipes1.py", title="Equipes", icon="👥")
agua_links = st.Page("agua/Links1.py", title="Links", icon="🔗")
agua_coleta_dados = st.Page("agua/Coleta_Dados1.py", title="Coleta de Dados", icon="📊")


carbono_home = st.Page(page="carbono/Pegada_Carbono.py", title="Pegada de Carbono", icon="🌍")
carbono_equipes = st.Page(page="carbono/Equipes2.py", title="Equipes", icon="👥")
carbono_links = st.Page("carbono/Links2.py", title="Links", icon="🔗")
carbono_coleta_dados = st.Page("carbono/Coleta_Dados2.py", title="Coleta de Dados", icon="📊")


carbon_calc_br = st.Page("tools/Calculadora_Carbono_br.py", title="🇧🇷 Calculadora de Carbono", icon="🔢")
carbon_calc_fr = st.Page("tools/Calculadora_Carbono_fr.py", title="🇫🇷 Calculateur de Carbone", icon="🔢")

carbon_calc2_br = st.Page("tools/Calculadora_Carbono2_br.py", title="🇧🇷 Calculadora de Carbono da Escola", icon="🔢")
carbon_calc2_fr = st.Page("tools/Calculadora_Carbono2_fr.py", title="🇫🇷 Calculatrice de Carbone de l'École", icon="🔢")


carbon_calc3_br = st.Page("tools/Calculadora_Carbono3_br.py", title="🇧🇷 Calculadora de Carbono Individual Avançada", icon="🔢")

monitor_sustentabilidade = st.Page("tools/Acoes_Sustentabilidade.py", title="Ações de Sustentabilidade", icon="🌍")
simulacao_10anos = st.Page("tools/Simulacao.py", title="Simulação de Pegada de Carbono", icon="📈")
curupira_ia = st.Page("tools/Curupira.py", title="Curupira", icon="🪵")

# history = st.Page("tools/history.py", title="History", icon=":material/history:")


pg = st.navigation(
    {
        "Home": [principal,forum, programacao, ods],
        "Agua": [agua_home, agua_equipes, agua_links, agua_coleta_dados],
        "Carbono": [carbono_home, carbono_equipes,carbono_links, carbono_coleta_dados],
        "Tools": [carbon_calc_br, carbon_calc_fr, carbon_calc2_br, carbon_calc2_fr, simulacao_10anos, monitor_sustentabilidade, carbon_calc3_br],
    }
)
    


pg.run()