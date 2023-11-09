import os

class Config():
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
