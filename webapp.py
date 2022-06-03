from regex import P
import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
import json
import numpy as np

### Functions
def process_for_display(image_file):
    "Original picture :"
    image=Image.open(image_file)
    st.image(image,width=250)

    width=image.width
    height=image.height

    #Prepare API Call
    image_data = image_file.read()

    files = {'file': image_file.getvalue()}

    response = requests.post(
        url,
        files=files,
    )

    response = requests.post(url, files=files)

    dict=json.loads(response.text)

    #Display the response

    "---"

    if 'error' in dict.keys():
        "Sorry but .. I did not find any face on this picture. Try with another photo or another angle ?"
    else:
        #Text response
        f"This person is a {dict['ethnicity']} {dict['gender']} and is {dict['age']}."
        "Analyzed picture :"
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

        st.image(image,width=250)

### API URL
url = 'http://127.0.0.1:8000/file/'


### Display

'''
# Age, gender and ethnicity prediction
'''

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:
    process_for_display(image_file)
