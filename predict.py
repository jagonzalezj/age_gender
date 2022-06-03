import joblib
import numpy as np
import matplotlib.pyplot as plt
from get_data import get_data
from params import ETHNICITIES, GENDERS

def get_model(path_to_joblib):
    model = joblib.load(path_to_joblib)
    return model

def get_standard():
    data=get_data()
    standard=np.array(data['pixels'][500].tolist()).reshape((-1, 48, 48,1))
    return standard

def get_ethnicity_prediction(image,dict=ETHNICITIES):
    '''Ethnicity prediction with an image = array 48*48*1'''
    model=get_model("ethnicity_model.joblib")
    return dict[np.argmax(model.predict(image)[0])]

def get_gender_prediction(image,dict=GENDERS):
    '''Gender prediction with an image = array 48*48*1'''
    model=get_model("gender_model.joblib")
    return dict[np.round(model.predict(image)[0][0],0)]

if __name__ == "__main__":
    print('to be tested')
    image=get_standard()

    print(get_gender_prediction(image))
