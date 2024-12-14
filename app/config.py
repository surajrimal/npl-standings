import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_default_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///standings.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/team_images'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    NEWS_BASE_URL_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_BASE_EVERYTHING_URL = 'https://newsapi.org/v2/everything?domains={}&apiKey={}'
    NEWS_BASE_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_BASE_SOURCE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    API_KEY = "8ea84fc5f129443a8078e6aba9bff126"