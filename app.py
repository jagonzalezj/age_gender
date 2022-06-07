from distutils.command.upload import upload
from multiprocessing.spawn import prepare
from jmespath import search
from matplotlib import container
import streamlit as st
import pandas as pd
import json
import requests
from PIL import Image, ImageDraw, ImageFont
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from webapp import get_api_response, get_image_from_response, get_text_from_response

def welcome():
    st.markdown("<h1 style='text-align: center;'>Bienvenue à tous</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Model de reconnaissance faciale</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Age - Genre - Ethnie</h2>", unsafe_allow_html=True)

    lottie_hello = load_lottiefile('./Lottie/hello.json')
    return st_lottie(lottie_hello)

def story_usage():
    st.markdown("<h1 style='text-align: center;'>Usages possibles</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Analyse de Profils")
        lottie_false = load_lottiefile('Lottie/faux_docs.json')
        st_lottie(lottie_false)
    with col2:
        st.header("Aide à l'authentification ")
        lottie_doc = load_url('https://assets6.lottiefiles.com/packages/lf20_cznnfmoz.json')
        st_lottie(lottie_doc)
    with col3:
        st.header("Identification")
        lottie_tinder = load_lottiefile('Lottie/identity.json')
        st_lottie(lottie_tinder)

    col4, col5,col6 = st.columns(3)
    with col4:
        st.text('média social, Tinder')
    with col5:
        st.text('faux passport')
    with col6:
        st.text('statistique évènement')

def the_idea():
    st.markdown("<h1 style='text-align: center;'>L'idée derrière le Projet</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.text("A partir d'une photo")
        lottie_camera = load_lottiefile('Lottie/camera.json')
        st_lottie(lottie_camera)
    with col2:
        st.text("Réussir à déterminer")
        lottie_arrow = load_lottiefile('Lottie/arrow.json')
        st_lottie(lottie_arrow)
    with col3:
        st.text("l'age, le sex et l'ethnie")
        lottie_sag = load_lottiefile('Lottie/sex_age_gender.json')
        st_lottie(lottie_sag)

def uploading():
    st.markdown("<h1 style='text-align: center;'>Téléchargement de l'image</h1>", unsafe_allow_html=True)
    image_file=st.file_uploader('Uploading a picture')

    if image_file is not None:
        st.text('Original picture')
        image=Image.open(image_file)
        st.image(image,width=250)

        st.text('Prediction')
        "---"
        response=get_api_response(image_file)
        get_image_from_response(response,image_file)
        get_text_from_response(response)

def live_test():
    st.markdown("<h1 style='text-align: center;'>Let's go for an experiment ?!</h1>", unsafe_allow_html=True)
    image_file_live=st.camera_input("Take a picture")

    "---"

    if image_file_live is not None:
        response=get_api_response(image_file_live)
        get_image_from_response(response,image_file_live)
        get_text_from_response(response)

def explanation():
    col1, col2 = st.columns(2)
    with col1:
        lottie_how = load_lottiefile('Lottie/question.json')
        st_lottie(lottie_how)
    with col2:
        st.title('Comment ça fonctionne ?')
    "***********"

    col3, col4 = st.columns(2)
    with col3:
        lottie_data = load_lottiefile('Lottie/data_scanning.json')
        st_lottie(lottie_data)
    with col4:
        st.title("Recherche des données")


    col7, col8,col9,col10 = st.columns(4)
    with col7:
        st.image('Notebook images/google_dataset_search.png')
    with col8:
        st.image('Notebook images/kaggle.png')
    with col9:
        st.image('Notebook images/source-github-1.jpg')
    with col10:
        st.image('Notebook images/utkface.png')

    data = st.container()
    correspondance = st.container()
    with data:
        st.image('Notebook images/dataset.png')
        st.image('Notebook images/correspondance_dataset.png')

    "***********"

    col11, col12 = st.columns(2)
    with col11:
        lottie_preproc = load_lottiefile('Lottie/preprocessing.json')
        st_lottie(lottie_preproc)
    with col12:
        st.title("Analyse et traitement")

    col16, col17, col18,  = st.columns(3)
    with col16:
        st.image('Notebook images/Initial_age_distribution.png')
    with col17:
        st.image('Notebook images/filtered_age_distribution.png')
    with col18:
        st.image('Notebook images/categorical_age_distribution.png')

    col13, col14 = st.columns(2)
    with col13:
        st.image('Notebook images/ethnicity_2.png')
    with col14:
        st.image('Notebook images/ethnicity_1.png')


    gender = st.container()
    with gender:
        st.image('Notebook images/gender_distribution.png')

    "***********"

    col19, col20 = st.columns(2)
    with col19:
        lottie_deep = load_lottiefile('Lottie/network.json')
        st_lottie(lottie_deep)
    with col20:
        st.title("Construction de l'algorythme")

    col21, col22, col23 = st.columns(3)
    with col21:
        st.image('Notebook images/algo_1.png')
    with col22:
        st.image('Notebook images/algo_2.png')
    with col23:
        st.image('Notebook images/machine-learning-reseau-neurones.png')

    col24, col25, col26 = st.columns(3)
    with col24:
        st.title("Data to model")
        lottie_tomodel = load_lottiefile('Lottie/data_to_model.json')
        st_lottie(lottie_tomodel)
    with col25:
        lottie_arrow = load_lottiefile('Lottie/arrow.json')
        st_lottie(lottie_arrow)
    with col26:
        st.title("and model Training")
        lottie_training = load_lottiefile('Lottie/model_training.json')
        st_lottie(lottie_training)

    "***********"
    col27, col28 = st.columns(2)
    with col27:
        lottie_estimator = load_lottiefile('Lottie/estimator.json')
        st_lottie(lottie_estimator)
    with col28:
        st.title("Analyse des perfomances")
    st.title('Les performances par catégories')

    ethnie = st.container()
    age = st.container()
    genre = st.container()

    with ethnie:
        st.markdown("<h3 style='text-align: center;'> Courbe d'apprentissage de l'ethnie </h3>", unsafe_allow_html=True)
        st.image('Notebook images/ethnie_histo.png')


    with age:
        st.markdown("<h3 style='text-align: center;'> Courbe d'apprentissage de l'age </h3>", unsafe_allow_html=True)
        st.image('Notebook images/age_histo.png')


    with genre:
        st.markdown("<h3 style='text-align: center;'> Courbe d'apprentissage du genre </h3>", unsafe_allow_html=True)
        st.image('Notebook images/gender_histo.png')

    st.markdown("<h3 style='text-align: left;'>Precision de la prédiction du genre = 87 % </h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left;'>Precision de la prédiction de l'ethnie = 81 %</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left;'>Precision de la catégorie d'âge = 82 %</h3>", unsafe_allow_html=True)

def not_easy():
    col1, col2 = st.columns(2)
    with col1:
        st.image('Notebook images/javier.png')
    with col2:
        st.image('Notebook images/pierre.png')
    col3, col4 = st.columns(2)
    with col3:
        st.image('Notebook images/paul_pres.png')
    with col4:
        st.image('Notebook images/pierre_lunette.png')
    col5, col6 = st.columns(2)
    with col5:
        st.image('Notebook images/indian_true.png')
    with col6:
        st.image('Notebook images/indian_pred.png')

    explication = st.container()
    with explication:
        #st.title('principale difficulté')
        st.markdown("<h1 style='text-align: center;'>Principale difficulté</h1>", unsafe_allow_html=True)

        #st.text("Estimation de l'âge")
        st.markdown("<h3 style='text-align: center;'>Estimation de l'âge</h3>", unsafe_allow_html=True)

        #st.title("Qu'avons-nous fait? ")
        st.markdown("<h1 style='text-align: center;'>Qu'avons-nous fait?</h1>", unsafe_allow_html=True)

        st.markdown("<h3 style='text-align: center;'>Plusieurs transformations du dataset dont :</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Réduction des données d'un an</li><i></h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Suppression des données supérieur à 80 ans</li><i></h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Regroupement par tranche d'âges </li><i></h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Supression des données d'un an</li><i></h3>", unsafe_allow_html=True)


#fin de la présentation
def thank_you():
    st.markdown("<h1 style='text-align: center;'>Vos Intervenants</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Javier")
        st.image('Intervenants/javier_pred.png')
    with col2:
        st.header("Paul")
        st.image('Intervenants/paul_pred.png')
    with col3:
        st.header("Pierre")
        st.image('Intervenants/pierre_pred.png')

#thème du sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Bienvenue", "L'idée", "Le rendu final", "Via téléchargement",
        "Live", "Explication","Pas si simple en réalité", "Merci"]
    )

#téléchargement des images et animation lottie
def load_lottiefile(filepath : str):
    with open(filepath, 'r') as f:
        return json.load(f)

def load_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#sidebar sélection
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
