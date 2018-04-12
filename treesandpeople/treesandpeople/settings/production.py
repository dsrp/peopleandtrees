import environ

from common import *  # noqa

env = environ.Env()

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

SECRET_KEY = env('DJANGO_SECRET_KEY')

# Cached template loader
# TEMPLATES[0]['OPTIONS']['loaders'] = [
#     ('django.template.loaders.cached.Loader', [
#         'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
# ]
