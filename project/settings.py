import os
import dj_database_url


from environs import Env

from dotenv import load_dotenv

env = Env()
env.read_env()
load_dotenv()

DB_URL = os.getenv('DB_URL')

DATABASES = {'default': dj_database_url.config(default=DB_URL)}
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = env.bool('DEBUG_DJANGO', 'False')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
