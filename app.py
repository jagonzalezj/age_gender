from distutils.command.upload import upload
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
    lottie_hello = load_lottiefile('./Lottie/hello.json')
    st_lottie(lottie_hello)
    st.markdown("<h2 style='text-align: center;'>Modèle de reconnaissance faciale</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Age - Sexe</h2>", unsafe_allow_html=True)





def story_usage():
    st.markdown("<h1 style='text-align: center;'>Usages possibles</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Analyse de profils")
        lottie_false = load_lottiefile('Lottie/faux_docs.json')
        st_lottie(lottie_false)
    with col2:
        st.header("Aide pour authentifier")
        lottie_doc = load_url('https://assets6.lottiefiles.com/packages/lf20_cznnfmoz.json')
        st_lottie(lottie_doc)
    with col3:
        st.header("Comptage")
        lottie_tinder = load_lottiefile('Lottie/identity.json')
        st_lottie(lottie_tinder)

    col4, col5,col6 = st.columns(3)
    with col4:

        st.text('Média social')
    with col5:
        st.text('Faux passport')
    with col6:
        st.text('Statistique évènement')


def the_idea():
    st.markdown("<h1 style='text-align: center;'>L'idée derrière le Projet</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.text("   A partir d'une photo")
        lottie_camera = load_lottiefile('Lottie/camera.json')
        st_lottie(lottie_camera)
    with col2:
        st.text("    Réussir à déterminer")
        lottie_arrow = load_lottiefile('Lottie/arrow.json')
        st_lottie(lottie_arrow)
    with col3:
        st.text("     l'âge et le sexe")
        lottie_age_sex = load_lottiefile('Lottie/sex_age_gender.json')
        st_lottie(lottie_age_sex)


def uploading():
    col5, col6 = st.columns(2)
    with col5:
        st.image('Notebook images/mulan.png')
    with col6:
        st.image('Notebook images/harry_p.png')

    st.markdown("<h1 style='text-align: center;'>Téléchargement de l'image</h1>", unsafe_allow_html=True)


    "---"

    image_file=st.file_uploader('Choisissez Une image')

    if image_file is not None:
        st.text('Image Original')
        image=Image.open(image_file)
        st.image(image,width=250)
        "---"
        st.text('Prediction')
        response=get_api_response(image_file)
        get_image_from_response(response,image_file,eth=False)
        get_text_from_response(response,eth=False)

def live_test():
    st.markdown("<h1 style='text-align: center;'>Expérience en direct</h1>", unsafe_allow_html=True)
    image_file_live=st.camera_input("Prendre un photo")

    "---"

    if image_file_live is not None:
        image=Image.open(image_file_live)
        response=get_api_response(image_file_live)
        get_image_from_response(response,image_file_live,eth=False)
        get_text_from_response(response,eth=False)
        st.text(max(image.getextrema()[0][1],image.getextrema()[1][1],image.getextrema()[2][1]))

def explanation():
    col1, col2 = st.columns(2)
    with col1:
        lottie_how = load_lottiefile('Lottie/question.json')
        st_lottie(lottie_how, speed=2, height=130)
    with col2:
        st.title('Comment ça fonctionne ?')
    "***********"
    #recherche de la donnée
    col3, col4, col5, col6 = st.columns(4)
    with col3:
        lottie_data = load_lottiefile('Lottie/data_scanning.json')
        st_lottie(lottie_data)
    with col4:
        st.title("Recherche des données")

    col7,col8 = st.columns(2)
    with col7:
        st.image('Notebook images/kaggle.png')
    with col8:
        st.image('Notebook images/utkface.png')

    # data = st.container()
    # with data:
    #     st.markdown('***24 000 images de personnes de 1 à 116 ans***')
    st.markdown("<h2 style='text-align: left;'>=> 24 000 images de personnes de 1 à 116 ans<i></h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: left;'>=> Hommes, femmes, enfants<i></h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: left;'>=> Appartenance ethnique(hors périmètre)<i></h2>", unsafe_allow_html=True)

    "***********"
    col9, col10, col11, col12 = st.columns(4)
    with col9:
        lottie_preproc = load_lottiefile('Lottie/preprocessing.json')
        st_lottie(lottie_preproc)
    with col10:
        st.title("Analyse et traitement")

    gender = st.container()
    with gender:
        st.image('Notebook images/sexe.png')

    histo = st.container()
    with histo:
        st.image('Notebook images/Age_original.png')
    age = st.container()
    with age:
        st.image('Notebook images/tranches_ages.png')

    "***********"

    col13, col14, col15, col16 = st.columns(4)
    with col13:
        lottie_deep = load_lottiefile('Lottie/network.json')
        st_lottie(lottie_deep)
    with col14:
        st.title("Construction de l'algorithme")

    preproc = st.container()
    with preproc:
        st.image('Notebook images/otra.png')

    softmax = st.container()
    with softmax:
        st.image('Notebook images/Image1_softmax.png')
    "********"
    linreg = st.container()
    with linreg:
        st.image('Notebook images/Image2_linreg.png')
    neuronnes = st.container()


    col17, col18, col19, col20,col21 = st.columns(5)
    with col18:
        st.title("Données")
        lottie_tomodel = load_lottiefile('Lottie/data_to_model.json')
        st_lottie(lottie_tomodel, speed=2, height=160)
    with col19:
        lottie_arrow = load_lottiefile('Lottie/arrow.json')
        st_lottie(lottie_arrow,speed=2)

    with col20:
        st.title("Modèle")
        lottie_training = load_lottiefile('Lottie/model_training.json')
        st_lottie(lottie_training, speed=3, height=130)


    "***********"
    col22, col23, col24,col25, col26 = st.columns(5)
    with col22:
        lottie_estimator = load_lottiefile('Lottie/estimator.json')
        st_lottie(lottie_estimator)
    with col23:
        st.title("Analyse des perfomances")

    # st.title("Exemple de visualisation de l'apprentissage")

    age = st.container()
    with age:
        # st.markdown("<h3 style='text-align: center;'> Courbe d'apprentissage de l'ethnie </h3>", unsafe_allow_html=True)
        st.image('Notebook images/courbe_apprentissage.png')

    st.markdown("<h3 style='text-align: left;'>==> Précision de la prédiction du sexe = 87 %<i></h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left;'>==> Précision de la catégorie d'âge = 82 %<i></h3>", unsafe_allow_html=True)
    "---"

def not_easy():
    col1, col2 = st.columns(2)
    with col1:
        st.header('Trop jeune')
        st.image('Notebook images/shakira.png')
    with col2:
        st.header('Trop âgé')
        st.image('Notebook images/pierre_2.png')

    col11, col12 = st.columns(2)
    with col11:
        st.header('Sexe masculin')
        st.image('Notebook images/angela.png')
    with col12:
        st.header('Erreur de détection')
        st.image('Notebook images/statue.png')

    explication = st.container()
    with explication:
        #st.title('principale difficulté')
        st.markdown("<h1 style='text-align: center;'>Principales difficultés</h1>", unsafe_allow_html=True)

        #st.text("Estimation de l'âge")
        st.markdown("<h3 style='text-align: center;'>Estimation de l'âge et passage sur des photos en live</h3>", unsafe_allow_html=True)

        #st.title("Qu'avons-nous fait? ")
        st.markdown("<h1 style='text-align: center;'>Qu'avons-nous fait?</h1>", unsafe_allow_html=True)

        st.markdown("<h3 style='text-align: center;'>Plusieurs transformations des données dont :</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Réduction des données des personnes < 5 ans</li><i></h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Suppression des données > 80 ans</li><i></h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Regroupement par tranche d'âges en amont de l'estimation de l'âge </li><i></h3>", unsafe_allow_html=True)


        st.markdown("<h3 style='text-align: center;'>Axes d'amélioration :</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Entraîner le modèle avec des images peu processées</li><i></h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Entraîner le modèle avec des angles et des luminosités plus variés</li><i></h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Utiliser un modèle en transfer learning</li><i></h3>", unsafe_allow_html=True)

        st.markdown("<h3 style='text-align: center;'>Ethique</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> <i><li>Extension à d'autres attributs</li><i></h3>", unsafe_allow_html=True)

#fin de la présentation
def thank_you():
    st.markdown("<h1 style='text-align: center;'>Vos Intervenants</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Javier")
        st.image('Intervenants/javier_1.png')
    with col2:
        st.header("Paul")
        st.image('Intervenants/paul_1.png')
    with col3:
        st.header("Pierre")
        st.image('Intervenants/pierre_3.png')

#thème du sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Bienvenue", "L'idée", "Usages possibles", "Via téléchargement",
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
    the_idea()

elif selected == "Usages possibles":
    story_usage()

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
