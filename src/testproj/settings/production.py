from decouple import Config, RepositoryEnv
from .common import *

# decouple, by default searches for .env files in repo root
# Need to point it in the right directory which is config/production.env
env_path = os.path.join(BASE_DIR,'..','..','config','production.env')

env_config = Config(RepositoryEnv(env_path))
SECRET_KEY = env_config.get('SECRET_KEY')
DEBUG = env_config.get('DEBUG',cast=bool)
# Allowed Hosts should be a list
ALLOWD_HOSTS = env_config.get('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

DATABASES = {
    'default': {
        'ENGINE': env_config.get('DB_ENGINE'),
        'NAME': env_config.get('DB_NAME'),
        'USER': env_config.get('DB_USER'),
        'PASSWORD': env_config.get('DB_PASSWORD'),
        'HOST': env_config.get('DB_HOST'),
        'PORT': env_config.get('DB_PORT')
    }
}