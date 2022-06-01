import os

from google.cloud import storage
from termcolor import colored

from params import BUCKET_NAME, MODEL_VERSION


def storage_upload(model_name,model_version=MODEL_VERSION, bucket=BUCKET_NAME, rm=False):
    client = storage.Client().bucket(bucket)
    filename=f"{model_name}.joblib"
    storage_location = 'models/{}/versions/{}/{}'.format(
        model_name,
        model_version,
        filename)
    blob = client.blob(storage_location)
    blob.upload_from_filename(filename)
    print(colored("=> {} uploaded to bucket {} inside {}".format(filename, BUCKET_NAME, storage_location),
                  "green"))
    if rm:
        os.remove(filename)
