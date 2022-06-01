from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from predict import get_model, get_standard, get_ethnicity_prediction, get_gender_prediction
from params import ETHNICITIES, GENDERS

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

    return {
        'age': "waiting for model",
        'gender':gender,
        'ethnicity':ethnicity
    }
