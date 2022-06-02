from regex import P
import streamlit as st
import datetime
import requests
import pandas as pd
from PIL import Image

'''
# Age, gender and ethnicity prediction
'''

image=st.file_uploader(label='Image à analyser')

image

url = 'http://127.0.0.1:8000/uploadfile/'
myobj = {'test_image': image}

# x = requests.post(url, files = myobj)

# print(x.text)

#Prepare Input
if image is not None:
    image_data = image.read()

# files = {'file': image_data}
files = {'file':(image_data, open(image_data, 'rb'), "image/jpeg")}
response = requests.post(url, files=files)

print(response.status_code, response.json())
