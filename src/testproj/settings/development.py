from decouple import Config, RepositoryEnv
from .common import *

# decouple, by default searches for .env files in repo root
# Need to point it in the right directory which is config/development.env
env_path = os.path.join(BASE_DIR,'..','..','config','development.env')

env_config = Config(RepositoryEnv(env_path))
SECRET_KEY = env_config.get('SECRET_KEY')
DEBUG = env_config.get('DEBUG',cast=bool)
# This should be blank for development
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': env_config.get('DB_ENGINE'),
        'NAME': os.path.join(BASE_DIR, env_config.get('DB_NAME')),
    }
}

