from .base import *  # noqa

# Read production env file
env.read_env(BASE_DIR / ".prodenv")

DEBUG = env('DEBUG', default=False)
SECURE_SSL_REDIRECT = env('SSL_REDIRECT', default=True)

ALLOWED_HOSTS = [
  'policycoding.com',
  'documentcoding.com',
  env('ADDITIONAL_ALLOWED_HOSTS', default=''),
]

CSRF_TRUSTED_ORIGINS = [
]
# AWS RDS Database
if 'RDS_DB_NAME' in env:
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': env('RDS_DB_NAME'),
      'USER': env('RDS_USERNAME'),
      'PASSWORD': env('RDS_PASSWORD'),
      'HOST': env('RDS_HOSTNAME'),
      'PORT': env('RDS_PORT'),
    }
  }
else:
  DATABASES = {
    'default': env.db()
  }

# Static/Media files - production paths
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '.static'

STATICFILES_FINDERS = [
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# Cache settings
CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    'LOCATION': 'cache_table',
  }
}
SOCIALACCOUNT_ONLY = True
# Google auth - production settings
SOCIALACCOUNT_PROVIDERS = {
  'google': {
    'APP': {
      'client_id': env('GOOGLE_CLIENT_ID'),
      'secret': env('GOOGLE_APP_SECRET'),
      'key': '',
    },
    'SCOPE': [
      'profile',
      'email',
    ],
    'AUTH_PARAMS': {
      'access_type': 'online',
    }
  }
}
