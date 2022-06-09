from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from predict import get_model, get_standard, get_ethnicity_prediction, get_gender_prediction, get_age_prediction
from params import ETHNICITIES, GENDERS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import io
import cv2

## Functions

## App

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello, this is the age_gender API"}

@app.get("/predict")
def predict():
    image=get_standard()
    ethnicity=get_ethnicity_prediction(image)

    gender=get_gender_prediction(image)

    age=get_age_prediction(image)

    return {
        'age': age,
        'gender':gender,
        'ethnicity':ethnicity
    }

@app.post("/file/")
# async def create_file(file):
#      return {"file_size": len(file)}
async def get_file(file: bytes = File(...)):
    stream = io.BytesIO(file)
    new_size=(48,48)

    image = np.array(Image.open(stream))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(image=image,scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))
    output_faces=[]

    if len(faces)==0 : return {'error':"no face found"}

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0),1)
        output_image = image[y:y + h, x:x + w]
        output_faces.append(f"{x}-{y}-{w}-{h}")

    image=cv2.resize(output_image, dsize=new_size, interpolation=cv2.INTER_CUBIC)

    image=np.mean(image, axis=2)

    image=Image.fromarray(np.uint8(image), 'L')

    image = image.resize(new_size)
    # image = Image.open(stream).resize(new_size)
    array=np.array(image.getdata()).reshape((-1, 48,48,1))


    ethnicity=get_ethnicity_prediction(array)
    gender=get_gender_prediction(array)
    age=get_age_prediction(array)
    # age="24"

    return {
        'age': f"{age} ans",
        'gender': gender,
        'ethnicity':ethnicity,
        'faces':'/'.join(output_faces)
    }
