import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/pitches'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig
}