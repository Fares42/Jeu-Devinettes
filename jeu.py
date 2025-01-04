import random
import streamlit as st

# Listes d'objets à deviner dans différentes catégories
categories = {
    "Animaux": ["chat", "chien", "éléphant", "girafe", "panda"],
    "Films": ["Transformers", "Avatar", "Titanic", "Star Wars", "Harry Potter"],
    "Lieux célèbres": ["Tour Eiffel", "Grand Canyon", "Taj Mahal", "Big Ben", "Dubai"],
    "Objets quotidiens": ["stylo", "clé", "téléphone", "chaussures", "lampe"],
    "Personnages célèbres": ["Albert Einstein", "Cristiano Ronaldo", "Barack Obama", "Michou", "Napoleon Bonaparte"]
}

# Fonction pour obtenir un indice basé sur le nombre d'essais
def donner_indice(reponse, essais):
    indices = {
        1: f"Le mot commence par '{reponse[0]}'.",
        2: f"Le mot a {len(reponse)} lettres.",
        3: f"Le mot contient la lettre '{random.choice(reponse)}'.",
        4: f"Le mot est un élément de la catégorie choisie.",
        5: "Pas d'autres indices disponibles. C'est ta dernière chance !"
    }
    return indices.get(essais, "Aucun indice disponible.")

# Initialiser l'état de l'application
if "category" not in st.session_state:
    st.session_state.category = None
if "reponse" not in st.session_state:
    st.session_state.reponse = None
if "essais" not in st.session_state:
    st.session_state.essais = 0

# Interface utilisateur
st.title("Jeu de Devinettes 🎲")
st.write("Devine un mot dans une catégorie donnée en moins de 5 essais !")

# Choix de la catégorie
if st.session_state.category is None:
    category = st.selectbox("Choisis une catégorie :", list(categories.keys()))
    if st.button("Commencer") and category:
        st.session_state.category = category
        st.session_state.reponse = random.choice(categories[category])
        st.session_state.essais = 0  # Réinitialisation des essais
        st.success(f"Je pense à un mot dans la catégorie '{category}'. Bonne chance !")

# Jeu en cours
else:
    guess = st.text_input("Essaie de trouver !")
    if st.button("Valider") and guess:
        st.session_state.essais += 1
        if guess.lower() == st.session_state.reponse.lower():
            st.success(f"Bravo ! Tu as deviné '{st.session_state.reponse}' en {st.session_state.essais} essais.")
            if st.button("Rejouer"):
                st.session_state.category = None  # Réinitialiser pour jouer à nouveau
        elif st.session_state.essais >= 5:
            st.error(f"Dommage, c'était facile ! La réponse était '{st.session_state.reponse}'.")
            if st.button("Rejouer"):
                st.session_state.category = None  # Réinitialiser pour jouer à nouveau
        else:
            st.warning(f"Mauvaise réponse. {donner_indice(st.session_state.reponse, st.session_state.essais)}")
