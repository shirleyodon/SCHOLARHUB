import os

class Config():
    BACKEND_HOST = os.environ.get('BACKEND_HOST')

    BACKEND_BASE_URL = f"http://{BACKEND_HOST}:5000/sh/"

    SECRET_KEY = "}c7@U4}C[rrXKS,r2Y+~E5O["
