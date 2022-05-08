import os

class Config:
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/pitches'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  
  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  # simple mde  configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
  pass

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/pitches_test'

class DevConfig(Config):
  '''
  Dev config child class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/pitches'
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}