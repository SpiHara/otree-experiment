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

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# 本番では環境変数から取得するのが推奨
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'admin')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'replace-with-your-own-secret-key'

INSTALLED_APPS = ['otree']

