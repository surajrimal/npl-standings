import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_default_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///standings.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/team_images'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}