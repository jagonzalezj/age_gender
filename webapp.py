from regex import P
import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
import json
import numpy as np
from params import api_url

### Functions
def get_api_response(image_file):

    #Prepare API Call

    files = {'file': image_file.getvalue()}

    response = requests.post(
        api_url,
        files=files,
    )

    dict=json.loads(response.text)

    return dict

def get_text_from_response(dict):

    if 'error' in dict.keys():
        st.write("Sorry but .. I did not find any face on this picture. Try with another photo or another angle ?")
    else:
        st.write(f"This person is a {dict['ethnicity']} {dict['gender']} and is {dict['age']}.")

def get_image_from_response(dict,image_file):
        image=Image.open(image_file)
        width=image.width
        height=image.height

        if 'error' in dict.keys():
            pass
        else:
            #Image response
            for face in dict['faces'].split('/'):
                face.split('-')

            face=dict['faces'].split('/')[-1]

            (x, y, w, h) = [int(i) for i in face.split('-')]

            start_point=(x,y)
            end_point=(x + w, y + h)
            font = ImageFont.truetype(font='arial.ttf',size=max(7,int(height/26)))
            #Draw rectangle
            ImageDraw.Draw(image).rectangle([start_point,end_point],
                            outline="black",
                            width=int(height/50))
            #Write attributes on the picture
            ImageDraw.Draw(image).text((int(width/50), int(height/50)),
                            dict['gender'],
                            font=font,
                            fill='rgb(0, 0, 0)')

            ImageDraw.Draw(image).text((int(width/50), int(height/15)),
                            dict['ethnicity'],
                            font=font,
                            fill='rgb(0, 0, 0)')

            ImageDraw.Draw(image).text((int(width/50), int(height-height/15)),
                            dict['age'],
                            font=font,
                            fill='rgb(0, 0, 0)')

            st.image(image,width=500)

### Display

'''
# Age, gender and ethnicity prediction
'''

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:
    "Original picture :"
    image=Image.open(image_file)
    st.image(image,width=250)

    response=get_api_response(image_file)
    get_image_from_response(response,image_file)
