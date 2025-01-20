import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:p%40ssword%C3%A9@localhost/housing")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
