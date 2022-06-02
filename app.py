from multiprocessing.spawn import prepare
import streamlit as st
import pandas as pd
import json
import requests

from streamlit_lottie import st_lottie

def load_lottiefile(filepath : str):
    with open(filepath, 'r') as f:
        return json.load(f)

def load_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


header = st.container()
story = st.container()
raw_images = st.container()
preprocessing = st.container()
exemple = st.container()
live = st.container()
estimation = st.container()
explication = st.container()
explication_2 = st.container()
echec = st.container()






with header :

    st.title('Bienvenue à tous')
    st.header('Notre à démo')
    st.header('AGE _GENDER_ETHNICITY RECOGNITION')

    lottie_hello = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/hello.json')
    st_lottie(lottie_hello)

    st.title('Usages possibles')
with story :

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




with story :

    st.title("L'idée du Projet")
    col1, col2, col3 = st.columns(3)

with col1:

    st.text("Photo prise en direct")
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

with live :
    st.title('Un ou Une volontaire ?')
    img_file = st.camera_input("Take a picture")

with estimation :
    st.title('Afficher le résultat')

with explication :
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
    st.text("2 : Analyser/traitement")
    # st.image("https://static.streamlit.io/examples/dog.jpg")
    lottie_prepro = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/preprocessing.json')
    st_lottie(lottie_prepro)

with col3:
    st.text("3 : Algorythme")
    # st.image("https://static.streamlit.io/examples/dog.jpg")
    lottie_deep = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/network.json')
    st_lottie(lottie_deep)

with explication_2 :

    col1, col2, col3 = st.columns(3)

with col1:

    st.text("4 : Data to machine")
    # st.image("https://static.streamlit.io/examples/cat.jpg")
    lottie_tomodel = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/data_to_model.json')
    st_lottie(lottie_tomodel)


with col2:
    st.text("5 : Entrainement du model")
    # st.image("https://static.streamlit.io/examples/dog.jpg")
    lottie_training = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/model_training.json')
    st_lottie(lottie_training)

with col3:
    st.text("6 : Resultat")
    # st.image("https://static.streamlit.io/examples/dog.jpg")
    lottie_estimator = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/estimator.json')
    st_lottie(lottie_estimator)


with echec :
    st.title("Tout n'a pas été un succès...")
    st.title("....loin de là ")
