from regex import P
import streamlit as st
import datetime
import requests
import pandas as pd
from PIL import Image

'''
# Age, gender and ethnicity prediction
'''

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:

        # To See details
        file_details = {"filename":image_file.name, "filetype":image_file.type,
                        "filesize":image_file.size}
        st.write(file_details)

        # To View Uploaded Image
        st.image(Image.open(image_file),width=250)

url = 'http://127.0.0.1:8000/file/'
myobj = {'test_image': image_file}

# x = requests.post(url, files = myobj)

# print(x.text)

#Prepare Input
if image_file is not None:
    image_data = image_file.read()

# files = {'file': image_data}
files = {'file':("test",image_data, "image/jpeg")}
response = requests.post(url, files=files)

print(response.status_code, response.json())
