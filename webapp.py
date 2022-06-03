from regex import P
import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
import json
import numpy as np

'''
# Age, gender and ethnicity prediction
'''

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:

        # To See details
        # file_details = {"filename":image_file.name, "filetype":image_file.type,
        #                 "filesize":image_file.size}
        # st.write(file_details)

        # To View Uploaded Image
        "Original picture :"
        image=Image.open(image_file)
        st.image(image,width=250)

        width=image.width
        height=image.height

url = 'http://127.0.0.1:8000/file/'
myobj = {'test_image': image_file}

#Prepare Input
if image_file is not None:
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

    response.status_code

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

        image.width
        image.height

        ImageDraw.Draw(image).rectangle([start_point,end_point],
                        outline="black",
                        width=int(height/50))

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
