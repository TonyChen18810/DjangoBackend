import os
from .base import *

os.environ.setdefault('WERKZEUG_DEBUG_PIN', 'off')

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
    'django_nose',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PANEL = [
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
    'cachalot.panels.CachalotPanel',
]

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-html',
    '--cover-erase',
    '--cover-package=base',
]

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '8431e342699a5c'
EMAIL_HOST_PASSWORD = '32f866789be6f9'
EMAIL_PORT = '2525'
