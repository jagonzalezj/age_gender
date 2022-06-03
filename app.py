from distutils.command.upload import upload
from multiprocessing.spawn import prepare
import streamlit as st
import pandas as pd
import json
import requests

from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


def welcome():

    st.title('Bienvenue à tous')
    st.header('Notre démo')
    st.header('AGE _GENDER_ETHNICITY RECOGNITION')
    lottie_hello = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/hello.json')
    return st_lottie(lottie_hello)

def story_usage():
    st.title('Usages possibles')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Analyse de Profils")
        # st.image("https://static.streamlit.io/examples/cat.jpg")
        lottie_false = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/faux_docs.json')
        st_lottie(lottie_false)

    with col2:
        st.header("Authetification ")
        # st.image("https://static.streamlit.io/examples/dog.jpg")
        lottie_doc = load_url('https://assets6.lottiefiles.com/packages/lf20_cznnfmoz.json')
        st_lottie(lottie_doc)

    with col3:
        st.header("Aide à l'indetification")
        # st.image("https://static.streamlit.io/examples/dog.jpg")
        lottie_tinder = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/identity.json')
        st_lottie(lottie_tinder)

def the_idea():
    st.title("L'idée derrière le Projet")
    col1, col2, col3 = st.columns(3)

    with col1:

        st.text("A partir d'une photo")
        # st.image("https://static.streamlit.io/examples/cat.jpg")
        lottie_camera = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/camera.json')
        st_lottie(lottie_camera)

    with col2:
        st.text("Réussir à déterminer")
        # st.image("https://static.streamlit.io/examples/dog.jpg")
        lottie_arrow = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/arrow.json')
        st_lottie(lottie_arrow)

    with col3:
        st.text("l'age, le sex et l'ethnie")
        # st.image("https://static.streamlit.io/examples/dog.jpg")
        lottie_sag = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/sex_age_gender.json')
        st_lottie(lottie_sag)

def uploading():
    st.title('Téléchargement')
    st.file_uploader('Télécharger une photo')

def live_test():
    st.title('Une Photo ?')
    st.camera_input("Take a picture")

def explanation():
    st.title('Comment ça fonctionne ?')
    lottie_how = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/question.json')
    st_lottie(lottie_how)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.text("1 : Recherche des données")
        # st.image("https://static.streamlit.io/examples/cat.jpg")
        lottie_data = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/data_scanning.json')
        st_lottie(lottie_data)


    with col2:
        st.text("2 : Analyser/traiter")
        # st.image("https://static.streamlit.io/examples/dog.jpg")
        lottie_prepro = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/preprocessing.json')
        st_lottie(lottie_prepro)

    with col3:
        st.text("3 : Algorythme")
        # st.image("https://static.streamlit.io/examples/dog.jpg")
        lottie_deep = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/network.json')
        st_lottie(lottie_deep)

def not_easy():
    pass

def thank_you():
    pass

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Bienvenue", "L'idée", "Le rendu final", "Via téléchargement",
        "Live", "Explication", "Pas si simple en réalité ", "Merci"]
    )



def load_lottiefile(filepath : str):
    with open(filepath, 'r') as f:
        return json.load(f)

def load_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()





if selected == "Bienvenue":
    welcome()

elif selected == "L'idée":
    story_usage()

elif selected == "Le rendu final":
    the_idea()

elif selected == "Via téléchargement":
    uploading()

elif selected == "Live":
    live_test()

elif selected == "Explication":
    explanation()

elif selected == "Pas si simple en réalité":
    not_easy()

elif selected == "Merci":
    thank_you()


    # st.title("Quelques utilisations : ")

    # st.text("Détection de faux documents")
    # lottie_false = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/faux_docs.json')
    # st_lottie(lottie_false)

    # st.text("aide à l'indetification ")
    # lottie_doc = load_url('https://assets6.lottiefiles.com/packages/lf20_cznnfmoz.json')
    # st_lottie(lottie_doc)

    # st.text("confirmation d'un profil")
    # lottie_tinder = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/identity.json')
    # st_lottie(lottie_tinder)




# with explication_2 :

#     col1, col2, col3 = st.columns(3)

# with col1:

#     st.text("4 : Data to machine")
#     # st.image("https://static.streamlit.io/examples/cat.jpg")
#     lottie_tomodel = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/data_to_model.json')
#     st_lottie(lottie_tomodel)


# with col2:
#     st.text("5 : Entrainement du model")
#     # st.image("https://static.streamlit.io/examples/dog.jpg")
#     lottie_training = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/model_training.json')
#     st_lottie(lottie_training)

# with col3:
#     st.text("6 : Resultat")
#     # st.image("https://static.streamlit.io/examples/dog.jpg")
#     lottie_estimator = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/estimator.json')
#     st_lottie(lottie_estimator)


# with echec :
#     st.title("Tout n'a pas été un succès...")
#     st.title("....loin de là")
