import joblib
import numpy as np
import matplotlib.pyplot as plt
from get_data import get_data
from params import ETHNICITIES, GENDERS, AGES, AGES_MAE

def get_model(path_to_joblib):
    model = joblib.load(path_to_joblib)
    return model

def get_standard():
    data=get_data()
    standard=np.array(data['pixels'][500].tolist()).reshape((-1, 48, 48,1))
    return standard

def get_ethnicity_prediction(image,dict=ETHNICITIES):
    '''Ethnicity prediction with an image = array 48*48*1'''
    image=image/255
    model=get_model("models/ethnicity_model.joblib")
    return dict[np.argmax(model.predict(image)[0])]

def get_gender_prediction(image,dict=GENDERS):
    '''Gender prediction with an image = array 48*48*1'''
    model=get_model("models/gender_model.joblib")
    return dict[np.round(model.predict(image)[0][0],0)]

def get_age_prediction(image,dict_age=AGES,dict_age_mae=AGES_MAE):
    '''Age interval prediction with an image = array 48*48*1'''
    model_cat=get_model("models/age_model_cat.joblib")
    image=image/255

    age_cat=dict_age[np.argmax(model_cat.predict(image)[0])]
    mae=dict_age_mae[np.argmax(model_cat.predict(image)[0])]

    model_label=f"models/age_model_{age_cat}.joblib"
    model_age_lin=get_model(model_label)

    age_prediction=np.round(model_age_lin.predict(image)[0][0],0)
    age_prediction_lower=max(0,age_prediction-mae)
    age_prediction_upper=age_prediction+mae

    return f"{age_prediction_lower} - {age_prediction_upper}"
    # return model_cat.predict(image)[0]

if __name__ == "__main__":
    print('to be tested')
    image=get_standard()

    print(get_gender_prediction(image))
