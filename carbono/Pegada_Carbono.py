import streamlit as st

st.set_page_config(page_title="Fórum França-Brasil", page_icon=":earth_americas:", layout="wide")


col_fr_title, col_br_title = st.columns(2)
with col_fr_title:
    st.title(":earth_africa: Empreinte Carbone")
with col_br_title:
    st.title(":earth_americas: Pegada de Carbono")

col_fr, col_br = st.columns([1, 1])

with col_fr:
    st.info(":green_heart: Comment diminuer son empreinte carbone par des solutions alternatives")
    st.markdown("""
    ### :bulb: **Calculs et approximations**
    Les calculs dans cette application sont basés sur des estimations générales et peuvent ne pas 
    refléter avec précision votre réalité individuelle. Par exemple, l'émission de CO2 par kWh 
    d'électricité est approximée à 0,5 kg, mais cela peut varier en fonction de la matrice 
    énergétique de chaque région. De même, les émissions des différents combustibles ou 
    des résidus sont généralement évaluées et peuvent changer selon l'efficacité du 
    véhicule ou les méthodes de traitement des déchets.

    ### :clipboard: **Détails des Émissions**
    Les calculs présents dans le code sont des approximations et ne sont pas nécessairement 
    basés sur des données réelles précises pour chaque situation spécifique. Examinons chaque type 
    d'émission :

    #### :zap: **Électricité**
    La valeur de 0,5 kg de CO2 par kWh est une moyenne couramment utilisée pour estimer 
    les émissions dans divers pays, mais la réelle émission dépend de la matrice énergétique locale. Les 
    pays utilisant principalement des énergies renouvelables (éolienne, solaire, hydroélectrique) auront 
    des émissions beaucoup plus faibles par kWh.

    #### :sun_with_face: **Énergie Solaire et Éolienne**
    Les facteurs de réduction sont des simplifications. En réalité, l'énergie 
    solaire et l'énergie éolienne peuvent avoir une empreinte carbone presque nulle, mais il y a de petites 
    émissions liées à la fabrication et à l'installation des équipements.

    #### :car: **Transport**
    Les estimations des émissions de CO2 par kilomètre pour les différents types de carburant 
    (Essence, Diesel, Alcool) sont approximatives et varient selon l'efficacité du véhicule, l'entretien et les 
    conditions de conduite. Par exemple, la valeur de 0,2 kg de CO2/km pour l'essence est une moyenne raisonnable, 
    mais les modèles plus modernes peuvent émettre moins, tandis que les véhicules plus anciens peuvent émettre plus.

    #### :wastebasket: **Résidus**
    L'estimation des émissions de résidus considère une moyenne de 0,1 kg de CO2 par kg de résidu. 
    Ceci est une simplification, car cela dépend fortement du type de résidu et de la méthode de traitement (par 
    exemple, incinération, décharge ou recyclage).

    #### :shallow_pan_of_food: **Alimentation**
    Les valeurs pour les régimes alimentaires (Omnivore, Végétarien, Végan) sont des généralisations 
    largement acceptées, mais peuvent encore varier en fonction de l'origine des aliments, de la saisonnalité et des 
    méthodes de production.

    ### :warning: **Note sur la Précision**
    Ainsi, ces calculs sont des simplifications basées sur des valeurs moyennes trouvées dans la littérature ou sur 
    des estimations communes des émissions. Pour obtenir une valeur plus précise, il serait nécessaire d'utiliser 
    des données spécifiques pour la localisation, les sources d'énergie, les types de véhicules et les habitudes 
    personnelles. Pour une utilisation plus rigoureuse et fiable, il est suggéré d'incorporer des données réelles 
    régionales ou sectorielles qui peuvent être trouvées dans des bases de données spécialisées ou des agences de 
    contrôle environnemental.
    """)

with col_br:
    st.info(":green_heart: Reduzindo sua pegada de carbono através de soluções alternativas")
    st.markdown("""
    ### :bulb: **Cálculos e Aproximações**
    Os cálculos desta aplicação são baseados em estimativas gerais e podem não 
    refletir com precisão sua realidade individual. Por exemplo, a emissão de CO2 
    por kWh de eletricidade é aproximada em 0,5 kg, mas isso pode variar de acordo 
    com a matriz energética de cada região. Da mesma forma, as emissões dos diferentes 
    combustíveis ou dos resíduos são avaliadas de forma geral e podem mudar conforme a 
    eficiência do veículo ou os métodos de tratamento de resíduos.

    ### :clipboard: **Detalhes das Emissões**
    Os cálculos presentes no código são aproximações e não necessariamente baseados em 
    dados reais precisos para cada situação específica. Vamos examinar cada uma das emissões:

    #### :zap: **Eletricidade**
    O valor de 0.5 kg de CO2 por kWh é uma média comum usada para estimar emissões em diversos 
    países, porém a real emissão depende da matriz energética local. Países que utilizam principalmente energia 
    renovável (eólica, solar, hidrelétrica) terão emissões muito menores por kWh.

    #### :sun_with_face: **Energia Solar e Eólica**
    Os fatores de redução são simplificações. Na realidade, a energia solar e eólica podem 
    ter uma pegada de carbono quase nula, mas há pequenas emissões ligadas à fabricação e instalação dos equipamentos.

    #### :car: **Transporte**
    As estimativas de emissões de CO2 por quilômetro para diferentes tipos de combustível (Gasolina, 
    Diesel, Álcool) são aproximadas e variam de acordo com a eficiência do veículo, manutenção e condições de condução. 
    Por exemplo, o valor de 0.2 kg de CO2/km para gasolina é uma média razoável, mas modelos mais modernos podem 
    emitir menos, enquanto veículos mais antigos podem emitir mais.

    #### :wastebasket: **Resíduos**
    A estimativa de emissões de resíduos considera a média de 0.1 kg de CO2 por kg de resíduo. Isso é 
    uma simplificação, pois depende muito do tipo de resíduo e da forma de tratamento (por exemplo, incineração, 
    aterro ou reciclagem).

    #### :shallow_pan_of_food: **Alimentação**
    Os valores para as dietas (Onívora, Vegetariana, Vegana) são generalizações amplamente aceitas, 
    mas ainda podem variar muito dependendo da origem dos alimentos, sazonalidade e métodos de produção.

    ### :warning: **Nota sobre a Precisão**
    Assim, esses cálculos são simplificações baseadas em valores médios encontrados na literatura ou em estimativas 
    comuns de emissões. Para obter um valor mais preciso, seria necessário utilizar dados específicos para a 
    localização, fontes de energia, tipos de veículos e hábitos pessoais. Para um uso mais rigoroso e confiável, 
    sugiro incorporar dados reais regionais ou setoriais que podem ser encontrados em bancos de dados especializados 
    ou agências de controle ambiental.
    """)

