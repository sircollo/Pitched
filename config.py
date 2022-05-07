import os

class Config:
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/pitches'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get('SECRET_KEY')

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