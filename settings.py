DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_rds_db_name',
        'USER': 'your_rds_db_user',
        'PASSWORD': 'your_rds_db_password',
        'HOST': 'your_rds_endpoint',
        'PORT': '5432',
    }
}

USE_I18N = True
USE_L10N = True
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
