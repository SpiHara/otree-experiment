from os import environ

SESSION_CONFIGS = [
    dict(
        name='my_experiment',
        display_name="My Experiment",
        app_sequence=['my_experiment'],
        num_demo_participants=1,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# Environment-based configuration for Render
LANGUAGE_CODE = environ.get('LANGUAGE_CODE', 'en')
REAL_WORLD_CURRENCY_CODE = environ.get('REAL_WORLD_CURRENCY_CODE', 'USD')
USE_POINTS = environ.get('USE_POINTS', 'true').lower() == 'true'

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'admin')

AUTH_LEVEL = environ.get('AUTH_LEVEL', None)

DEMO_PAGE_INTRO_HTML = """ """

# Use environment variable for secret key in production
SECRET_KEY = environ.get('SECRET_KEY', 'replace-with-your-own-secret-key')

INSTALLED_APPS = ['otree']

# Render-specific settings
if environ.get('RENDER'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': environ.get('DB_NAME', 'otree'),
            'USER': environ.get('DB_USER', 'otree'),
            'PASSWORD': environ.get('DB_PASSWORD', ''),
            'HOST': environ.get('DB_HOST', 'localhost'),
            'PORT': environ.get('DB_PORT', '5432'),
        }
    }
    
    STATIC_ROOT = 'staticfiles'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    DEBUG = False
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = True
