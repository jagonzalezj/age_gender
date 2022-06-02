import pandas as pd
import numpy as np

def get_data ():
    url = "raw_data/age_gender.csv"
    df = pd.read_csv(url)

    df['pixels'] = df['pixels'].apply(lambda x: np.array(x.split(),dtype='float32'))

    return df
