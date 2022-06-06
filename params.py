BUCKET_NAME="to_be_defined"
MODEL_VERSION="v0"

# Ethnicity labels
ETHNICITIES = {
    0: "White",
    1: "Black",
    2: "Asian",
    3: "Indian/Hispanic",
    4: "Hispanic"
}

# Gender labels
GENDERS = {
    0: "Male",
    1: "Female"
}

# Age labels
AGES= {
    0: "5_19",
    1: "20_49",
    2: "50_80",
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
api_url = 'http://127.0.0.1:8000/file/'
