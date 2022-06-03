from distutils.command.upload import upload
from multiprocessing.spawn import prepare
from jmespath import search
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
        lottie_false = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/faux_docs.json')
        st_lottie(lottie_false)

    with col2:
        st.header("Authetification ")
        lottie_doc = load_url('https://assets6.lottiefiles.com/packages/lf20_cznnfmoz.json')
        st_lottie(lottie_doc)

    with col3:
        st.header("Aide à l'indetification")
        lottie_tinder = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/identity.json')
        st_lottie(lottie_tinder)

def the_idea():
    st.title("L'idée derrière le Projet")
    col1, col2, col3 = st.columns(3)

    with col1:

        st.text("A partir d'une photo")
        lottie_camera = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/camera.json')
        st_lottie(lottie_camera)

    with col2:
        st.text("Réussir à déterminer")
        lottie_arrow = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/arrow.json')
        st_lottie(lottie_arrow)

    with col3:
        st.text("l'age, le sex et l'ethnie")
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
def recherche():
    st.text("1 : Recherche des données")
    lottie_data = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/data_scanning.json')
    st_lottie(lottie_data)
# 1 - visuel recherche des données
    col1, col2,col3,col4 = st.columns(4)
    with col1:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/google_dataset_search.png')
    with col2:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/kaggle.png')
    with col3:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/source-github-1.jpg')
    with col4:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/utkface.png')

def analyse():
    # 2 - visuel analyse des données
    st.text("2 : Analyser/traiter")
    lottie_preproc = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/preprocessing.json')
    st_lottie(lottie_preproc)

    col1, col2, col3,  = st.columns(3)
    with col1:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/ethnicity_distribution.png')

    with col2:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/ethnicity_distribution - Copie.png')
    with col3:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/ethnicity_distribution - Copie (2).png')

def algo():
# visuel construction de l'algorythme
    st.text("3 : Algorythme")
    lottie_deep = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/network.json')
    st_lottie(lottie_deep)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/algo_1.png')
    with col2:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/algo_2.png')
    with col3:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/reseaux_neurones_feed_forwarded_2.png')

def training():
# visuel entrainement
    col1, col2 = st.columns(2)
    with col1:
        st.text("4 : Data to machine")
        lottie_tomodel = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/data_to_model.json')
        st_lottie(lottie_tomodel)
    with col2:
        st.text("5 : Entrainement du model")
        lottie_training = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/model_training.json')
        st_lottie(lottie_training)
def perf ():
# afficher les performances
    st.text("6 : Resultat")
    lottie_estimator = load_lottiefile('/home/pablo/code/jagonzalezj/age_gender/Lottie/estimator.json')
    st_lottie(lottie_estimator)

    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/gender_loss_accuracy.png')
    with col2:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/gender_ytrue_ypredict.png')
    with col3:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/gender_ytrue_ypredict_0.png')
    with col4:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/gender_ytrue_ypredict_0.png')
    with col5:
        st.image('/home/pablo/code/jagonzalezj/age_gender/Notebook images/gender_ytrue_ypredict_0_0.png')


def not_easy():
    pass

def thank_you():
    pass
#     st.title('Vos intervenants')
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.header("Javier")
#         lottie_Javier = st.image('/home/pablo/code/jagonzalezj/age_gender/Intervenants/Javier.jpg')
#         st_lottie(lottie_Javier)

#     with col2:
#         st.header("Paul")
#         lottie_Paul = st.image('/home/pablo/code/jagonzalezj/age_gender/Intervenants/Paul.jpg')
#         st_lottie(lottie_Paul)

#     with col3:
#         st.header("Pierre")
#         lottie_Pierre = st.image('/home/pablo/code/jagonzalezj/age_gender/Intervenants/Pierre.jpg')
#         st_lottie(lottie_Pierre)

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Bienvenue", "L'idée", "Le rendu final", "Via téléchargement",
        "Live", "Explication", "Recherche de la données","Analyse", "Algorythme",
        "Entrainement", "Resultats","Pas si simple en réalité ", "Merci"]
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
elif selected == "Recherche de la données":
    recherche()
elif selected == "Analyse":
    analyse()
elif selected == "Algorythme":
    algo()
elif selected == "Entrainement":
    training()
elif selected == "Resultats":
    perf()

elif selected == "Pas si simple en réalité":
    not_easy()

elif selected == "Merci":
    thank_you()
