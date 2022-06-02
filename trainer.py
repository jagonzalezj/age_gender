### IMPORTS ###
## General librairies
from tkinter.simpledialog import askinteger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.cloud import storage
import joblib
from termcolor import colored
import ipdb

## Datascience imports
from tensorflow.keras import Sequential, layers
from tensorflow.keras import optimizers
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras import optimizers
from tensorflow.keras.optimizers.schedules import ExponentialDecay

## From current module
from image import pixel_mirroring
from gcp import storage_upload
from get_data import get_data

### CODE ###

## Model class

class Trainer(object):
    def __init__(self, data, local=True, **kwargs):
        self.local=local
        self.data=data
        self.es=EarlyStopping(monitor = 'val_accuracy',
                   mode = 'max',
                   patience = 10,  #to be modified to 10 in production
                   verbose = 0,
                   restore_best_weights = True)
        self.model=None
        self.history=None
        self.categorical_metrics=['accuracy','Recall','Precision']
        self.epochs=200  #to be modified to 200 in production
        self.y_train=None
        self.y_validation=None
        self.y_test=None
        self.X_train=None
        self.X_validation=None
        self.X_test=None

    def save_model(self, model_name, upload=False):
        """Save the model into a .joblib and upload it on Google Storage /models folder"""
        joblib.dump(self.model, f"{model_name}.joblib")
        print(colored(f"{model_name}.joblib saved locally", "green"))

        if upload:
            storage_upload(model_name)

    def evaluate(self):
        """Evaluate the model"""
        return print(self.model.evaluate(self.X_test,self.y_test,verbose=0))


## Ethnicity model

class TrainerEthnicity(Trainer):
    def __init__(self, data, **kwargs):
        super().__init__(data)

    def ethnicity_data_preparation(self):
        #Computing X and y
        X = self.data['pixels'].tolist()
        X = np.array(X).reshape((-1, 48, 48,1))
        y = to_categorical(self.data['ethnicity'],num_classes=5)

        #Splitting the data in order to oversize hispanics
        data_train, data_test, y_train, y_test = train_test_split(self.data, y, test_size=0.3, random_state=1)
        data_train, data_validation, y_train, y_validation =\
            train_test_split(data_train, y_train, test_size=0.2, random_state=1)

        whites=data_train[data_train['ethnicity']==0]
        blacks=data_train[data_train['ethnicity']==1]
        asians=data_train[data_train['ethnicity']==2]
        indians=data_train[data_train['ethnicity']==3]
        hispanics=data_train[data_train['ethnicity']==4]
        hispanics_mirrored=hispanics.copy()
        hispanics_mirrored['pixels']=hispanics_mirrored['pixels'].apply(pixel_mirroring)

        data_train=pd.concat([whites, blacks, asians, indians, hispanics, hispanics_mirrored])

        #Changing hispanics category to 3
        data_train['ethnicity'] = data_train['ethnicity'].replace(4,3)
        data_test['ethnicity'] = data_test['ethnicity'].replace(4,3)
        data_validation['ethnicity'] = data_validation['ethnicity'].replace(4,3)

        #Computing X, y for training, validation and test
        self.y_train= to_categorical(data_train['ethnicity'],num_classes=4)
        self.y_validation= to_categorical(data_validation['ethnicity'],num_classes=4)
        self.y_test= to_categorical(data_test['ethnicity'],num_classes=4)

        self.X_train= np.reshape(data_train['pixels'].tolist(), (-1, 48, 48,1))
        self.X_validation= np.reshape(data_validation['pixels'].tolist(), (-1, 48, 48,1))
        self.X_test= np.reshape(data_test['pixels'].tolist(), (-1, 48, 48,1))


    def ethnicity_initialize_model(self):

        model = Sequential()
        model.add(layers.Conv2D(128, (3,3), activation='relu', input_shape=(48,48,1)))
        model.add(layers.MaxPool2D(pool_size=(2,2)))

        model.add(layers.Conv2D(64, (3,3), activation='relu', padding='same'))
        model.add(layers.MaxPool2D(pool_size=(2,2)))

        model.add(layers.Conv2D(64,(3,3),activation='relu'))
        model.add(layers.MaxPooling2D(2,2))
    #     model.add(layers.Dropout(0.2))

        model.add(layers.Conv2D(32,(3,3),activation='relu'))
        model.add(layers.MaxPooling2D(2,2))
        model.add(layers.Dropout(0.1))

        model.add(layers.Flatten())
    #     model.add(layers.Dropout(0.5))

        model.add(layers.Dense(4, activation='softmax'))

        initial_learning_rate = 0.001 # start with default Adam value

        lr_schedule = ExponentialDecay(
            # Every 4000 iterations, multiply the learning rate by 0.7
            initial_learning_rate, decay_steps = 4000, decay_rate = 0.7,
        )

        opt = optimizers.Adam(learning_rate=lr_schedule)
        model.compile(loss='categorical_crossentropy',
                    optimizer=opt,
                    metrics=self.categorical_metrics)

        self.model=model

    def ethnicity_train_model(self, with_validation=True):
        if with_validation:
            history=self.model.fit(self.X_train,self.y_train,
                            validation_data=(self.X_validation,self.y_validation),
                            epochs=self.epochs,
                            batch_size=32,
                            callbacks=[self.es],
                            verbose=0)
        else:
            history=self.model.fit(self.X_train,self.y_train,
                            validation_split=0.2,
                            epochs=self.epochs,
                            batch_size=32,
                            callbacks=[self.es],
                            verbose=0)

        self.history=history

## Gender model

class TrainerGender(Trainer):
    def __init__(self, data, **kwargs):
        super().__init__(data)

    def gender_data_preparation(self):
        #Computing X and y
        X = np.array(self.data['pixels'].tolist())
        X = np.reshape(X, (-1, 48, 48,1))
        y = self.data['gender']

        #Creating train and test sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    def gender_initialize_model(self):
        model = Sequential()

        model.add(layers.Conv2D(64,(3,3),activation='relu',padding = "same",input_shape=(48,48,1)))
        model.add(layers.MaxPooling2D(2,2))

        model.add(layers.Conv2D(32,(3,3),activation='relu'))
        model.add(layers.MaxPooling2D(2,2))

        model.add(layers.Conv2D(64,(3,3),activation='relu'))
        model.add(layers.MaxPooling2D(2,2))

        model.add(layers.Conv2D(64,(3,3),activation='relu'))
        model.add(layers.MaxPooling2D(2,2))

        model.add(layers.Flatten())

        model.add(layers.Dense(1,activation='sigmoid'))

        model.compile(optimizer='adam' ,loss='BinaryCrossentropy',
                            metrics=self.categorical_metrics)

        self.model=model

    def gender_train_model(self,with_validation=True):
        if with_validation:
            history=self.model.fit(self.X_train,self.y_train,
                            validation_data=(self.X_validation,self.y_validation),
                            epochs=self.epochs,
                            batch_size=32,
                            callbacks=[self.es],
                            verbose=0)
        else:
            history=self.model.fit(self.X_train,self.y_train,
                            validation_split=0.2,
                            epochs=self.epochs,
                            batch_size=32,
                            callbacks=[self.es],
                            verbose=0)

        self.history=history

if __name__ == "__main__":
    print("############   Loading Data   ############")
    data = get_data()
    # data=pd.read_csv('./raw_data/age_gender.csv')
    # data['pixels']=data['pixels'].apply(lambda x:  np.array(x.split(), dtype="float32"))

    ethnicity = TrainerEthnicity(data=data)
    gender = TrainerGender(data=data)
    age = 0
    print("data loaded")

    print(colored("############  Ethnicity model   ############", "red"))

    ethnicity.ethnicity_data_preparation()
    ethnicity.ethnicity_initialize_model()
    print("Starting training")
    ethnicity.ethnicity_train_model()
    print("Ending training")
    ethnicity.evaluate()
    ethnicity.save_model("ethnicity_model")

    print(colored("############  Gender model ############", "blue"))

    gender.gender_data_preparation()
    gender.gender_initialize_model()
    print("Starting training")
    gender.gender_train_model(with_validation=False)
    print("Ending training")
    gender.evaluate()
    gender.save_model("gender_model")

    # print(colored("############   Age model    ############", "green"))

    # age.age_data_preparation()
    # age.age_initialize_model()
    # print("Starting training")
    # age.age_train_model()
    # print("Ending training")
    # age.evaluate()
    # age.save_model("age_model")
