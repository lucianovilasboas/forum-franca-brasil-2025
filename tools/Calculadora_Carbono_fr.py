import streamlit as st
import math

st.set_page_config(page_title="Forum France-Brésil", page_icon=":earth_americas:", layout="wide")

# =====================================
# Fonctions pour équivalences
# =====================================
def calculer_equivalence_arbres(emission_totale):
    # Environ un arbre absorbe 21 kg de CO2 par an
    return emission_totale / 21

def calculer_equivalence_voitures(emission_totale):
    # Une voiture émet environ 12 000 kg de CO2 par an
    return emission_totale / 12000

# =====================================
# En-tête
# =====================================
st.title(":deciduous_tree: Calculatrice d'Empreinte Carbone :earth_africa:")
st.markdown("""
## Estimez vos émissions et découvrez votre impact sur la planète !
Cette calculatrice vous aide à comprendre la quantité de CO2 que vous générez par mois
et fournit des équivalences pour des actions durables.
""")

# =====================================
# Section 1 - Énergie et électricité
# =====================================
st.header("1. Énergie et Électricité")
electricite = st.number_input("Consommation mensuelle d'électricité (kWh) :", min_value=0.0, step=1.0)
emission_electricite = electricite * 0.5  # Émission moyenne par kWh (en kg de CO2)

energie_solaire = st.checkbox("Utilisez-vous l'énergie solaire ?")
if energie_solaire:
    emission_electricite *= 0.2  # Réduction si énergie solaire

energie_eolienne = st.checkbox("Utilisez-vous l'énergie éolienne ?")
if energie_eolienne:
    emission_electricite *= 0.1  # Réduction encore plus importante si énergie éolienne

# =====================================
# Section 2 - Transport
# =====================================
st.header("2. Transport")
km_voiture = st.number_input("Kilomètres parcourus en voiture par mois :", min_value=0.0, step=1.0)
type_carburant = st.selectbox("Type de carburant :", ["Essence", "Diesel", "Alcool"])

if type_carburant == "Essence":
    emission_voiture = km_voiture * 0.2  # Émission moyenne pour essence (kg CO2 par km)
elif type_carburant == "Diesel":
    emission_voiture = km_voiture * 0.27  # Émission moyenne pour diesel
else:
    emission_voiture = km_voiture * 0.1  # Émission moyenne pour alcool

# =====================================
# Section 3 - Déchets
# =====================================
st.header("3. Déchets")
quantite_dechets = st.number_input("Quantité de déchets produits par semaine (kg) :", min_value=0.0, step=1.0)
emission_dechets = quantite_dechets * 4 * 0.1  # Approximation mensuelle pour CO2 par kg de déchet

# =====================================
# Section 4 - Alimentation
# =====================================
st.header("4. Alimentation")
diete = st.selectbox("Quel est votre type de régime alimentaire ?", ["Omnivore", "Végétarien", "Vegan"])

if diete == "Omnivore":
    emission_alimentation = 300  # Approximation mensuelle en kg de CO2
elif diete == "Végétarien":
    emission_alimentation = 200
else:
    emission_alimentation = 150

# =====================================
# Calcul des émissions totales
# =====================================
emission_totale = emission_electricite + emission_voiture + emission_dechets + emission_alimentation

# Équivalences
equivalence_arbres = calculer_equivalence_arbres(emission_totale)
equivalence_voitures = calculer_equivalence_voitures(emission_totale)

# =====================================
# Résultats
# =====================================
st.markdown("""
## :bar_chart: Résultats
""")
st.write(f"**Émissions liées à l'électricité :** {emission_electricite:.2f} kg CO2 par mois")
st.write(f"**Émissions liées au transport :** {emission_voiture:.2f} kg CO2 par mois")
st.write(f"**Émissions liées aux déchets :** {emission_dechets:.2f} kg CO2 par mois")
st.write(f"**Émissions liées à l'alimentation :** {emission_alimentation:.2f} kg CO2 par mois")
st.markdown(f"### :sparkles: **Émission totale estimée :** {emission_totale:.2f} kg CO2 par mois")

# =====================================
# Équivalences durables
# =====================================
st.markdown("---")
st.markdown("## :seedling: Actions durables équivalentes")
st.write(f":deciduous_tree: **Nombre d'arbres nécessaires pour absorber cette quantité de CO2 en un an :** {math.ceil(equivalence_arbres):,} arbres")
st.write(f":car: **Équivalent à l'impact de {equivalence_voitures:.2f} voitures par an**")

# =====================================
# Conseils
# =====================================
st.markdown("---")
st.markdown("### :bulb: **Conseils pour réduire votre empreinte carbone :**")
st.markdown("""
- Réduisez la consommation d'électricité en éteignant les appareils non utilisés.
- Utilisez des moyens de transport plus durables, comme le vélo ou les transports publics.
- Essayez de réduire le gaspillage alimentaire et augmentez le recyclage.
- Envisagez d'adopter un régime davantage basé sur les végétaux.
""")

# =====================================
# Barre de progression
# =====================================
st.markdown("---")
st.markdown("### :dart: **Progression par rapport à l'impact du CO2**")
st.progress(emission_totale / 1000, text=f"Émission Totale : {emission_totale:.2f} kg CO2")

# =====================================
# Avis et limitations
# =====================================
st.write("---")
st.markdown("### Limitations et avertissements")
st.caption("⚠️ Cette calculatrice est un prototype éducatif avec des estimations simplifiées. Pour des inventaires officiels, suivez le GHG Protocol, ISO 14064/14067 et d'autres normes internationales.")
