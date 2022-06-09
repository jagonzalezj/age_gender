BUCKET_NAME="to_be_defined"
MODEL_VERSION="v0"

# Ethnicity labels
ETHNICITIES = {
    0: "blanche",
    1: "noire",
    2: "asiatique",
    3: "indienne/hispanique",
    4: "hispanique"
}

# Gender labels
GENDERS = {
    0: "Homme",
    1: "Femme"
}

# Age labels
AGES= {
    0: "5_24",
    1: "25_39",
    2: "40_80",
    3: "60_80",
}

# Age linear model MAE
AGES_MAE= {
    0: 2,
    1: 4,
    2: 6,
    3: 0,
}

# API URL
api_url = 'https://api-online-v2-b7bsb3t4hq-od.a.run.app/file/'
