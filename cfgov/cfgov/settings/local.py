from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CFGOV_REFRESH = Path(__file__).ancestor(5).child('cfgov-refresh')

GRUNT_WATCH = [CFGOV_REFRESH]

DEBUG = True


ALLOWED_HOSTS = ['*']

# Application definition


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'



SHEER_SITES=[CFGOV_REFRESH.child('dist')]
SHEER_ELASTICSEARCH_SERVER = 'localhost:9200'
SHEER_ELASTICSEARCH_INDEX = 'content'
