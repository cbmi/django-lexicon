import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'tests.db'),
    }
}

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'avocado',
    'tests',
)

ROOT_URLCONF = 'tests.urls'

SOUTH_TESTS_MIGRATE = False

SECRET_KEY = 'abc123'
