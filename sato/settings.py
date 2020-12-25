# In production: SECRET_KEY, DATABASES and LOGGING are different
import os
gettext = lambda s: s
_ = lambda s: s

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRES_DB = {
    'CONN_MAX_AGE': 0,
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.getenv('POSTGRES_NAME', 'kubernetes_django'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    'USER': os.getenv('POSTGRES_USER'),
    'HOST': os.getenv('POSTGRES_HOST'),
    'PORT': os.getenv('POSTGRES_PORT', 5432)
}

SQLITE_DB = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}

# ENVIRONMENT SETTINGS
# ====================

# Use production settings if the environment variable is set
if 'DJANGO_PRODUCTION' in os.environ and os.getenv('DJANGO_PRODUCTION') == "1":
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    THUMBNAIL_DEBUG = False

    DATABASES = {
        'default': POSTGRES_DB
    }

    # Private filer files for Nginx
    FILER_SERVERS = {
        'private': {
            'main': {
                'ENGINE': 'filer.server.backends.nginx.NginxXAccelRedirectServer',
                'OPTIONS': {
                    'location': '/usr/src/app/smedia/filer_private',
                    'nginx_location': '/smedia',
                },
            },
            'thumbnails': {
                'ENGINE': 'filer.server.backends.nginx.NginxXAccelRedirectServer',
                'OPTIONS': {
                    'location': '/usr/src/app/smedia/filer_thumbnails_private',
                    'nginx_location': '/sthumbnails',
                },
            },
        },
    }

    # Use HTTPS as the redirect protocol in production
    SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

    # Email settings
    EMAIL_HOST = 'smtp.eu.mailgun.org'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.getenv('EMAIL_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')

    SERVER_EMAIL = 'django@mail.satakuntatalo.fi'
    DEFAULT_FROM_EMAIL = 'noreply@mail.satakuntatalo.fi'
    ADMINS = [('DjangoAdmin', os.getenv('DJANGO_ADMIN_EMAIL', 'localhost'))]

else:  # Development settings
    SECRET_KEY = 'verisecriit'
    DEBUG = True
    THUMBNAIL_DEBUG = True

    # Database
    DATABASES = {
        'default': POSTGRES_DB if 'POSTGRES_HOST' in os.environ else SQLITE_DB
    }

    DEFAULT_FILER_SERVERS = {
        'private': {
            'main': {
                'ENGINE': 'filer.server.backends.default.DefaultServer',
            },
            'thumbnails': {
                'ENGINE': 'filer.server.backends.default.DefaultServer',
            }
        }
    }

# COMMON SETTINGS
# ===============

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'django-service',
    'django.satakuntalainenosakunta.fi',
]

# Application definition
ROOT_URLCONF = 'sato.urls'
WSGI_APPLICATION = 'sato.wsgi.application'
LOGIN_URL = '/login/auth0/'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_TRAILING_SLASH = True
SOCIAL_AUTH_AUTH0_DOMAIN = 'osakunta.eu.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = '7BDybKqufcGKGszPSpTiSbs3oD044oD4'
SOCIAL_AUTH_AUTH0_SECRET = os.getenv('AUTH0_CLIENT_SECRET')

SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email'
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

AUTHENTICATION_BACKENDS = {
    'auth0login.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend'
}

# Internationalization
LANGUAGE_CODE = 'fi'
TIME_ZONE = 'Europe/Helsinki'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'sato', 'static'),
    os.path.join(BASE_DIR, 'palautteet', 'hairinta', 'static'),
    #('gallery-images', '../gallery-images/')
)

STATICFILES_FINDERS = [
    # For Aldryn blog
    'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

SITE_ID = 1
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'sato', 'templates'),
            os.path.join(BASE_DIR, 'gallery', 'templates'),
            os.path.join(BASE_DIR, 'auth0login', 'templates'),
            os.path.join(BASE_DIR, 'palautteet', 'templates'),
            os.path.join(BASE_DIR, 'palautteet', 'hallitus', 'templates'),
            os.path.join(BASE_DIR, 'palautteet', 'hairinta', 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'aldryn_boilerplates.context_processors.boilerplate',  # For Aldryn blog
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',  # For Aldryn blog
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'filer',
    'djangocms_file',
    'easy_thumbnails',
    'social_django',
    'sato',
    'auth0login',

    # Raw HTML for quick fixes
    'cmsplugin_raw_html',
    'djangocms_column',

    # For Aldryn blog
    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'parler',
    'sortedm2m',
    'taggit',

    # In-house-apps
    'ilmo_app',
    'gallery',
    'cmsplugin_content_wrappers',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'console_on_not_debug': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'console_on_not_debug'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

LANGUAGES = (
    ('fi', gettext('suomi')),
    ('sv', gettext('svenska')),
    ('en', gettext('English')),
)

CMS_LANGUAGES = {
    1: [
        {
            'redirect_on_fallback': True,
            'code': 'fi',
            'hide_untranslated': False,
            'name': gettext('suomi'),
            'public': True,
        },
        {
            'code': 'sv',
            'name': gettext('svenska'),
            'fallbacks': ['fi'],
            'public': True,
        },
        {
            'code': 'en',
            'name': gettext('English'),
            'fallbacks': ['fi'],
            'public': True,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ('page.html', 'Page'),
    ('page_bare.html', 'Page without content wrapper'),
    ('feature.html', 'Page with Feature'),
    ('specific-pages/homepage.html', 'Etusivun pohja'),
    ('specific-pages/calendar.html', 'Kalenterin pohja'),
    ('specific-pages/ajankohtaista.html', 'Artikkelipohja'),
    ('specific-pages/yhteystiedot.html', 'Yhteystietojen pohja'),
)

DJANGOCMS_STYLE_CHOICES = [
    'content-bg',
    'container',
    'row',
]

CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}

MIGRATION_MODULES = {}

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CMS',
}

THUMBNAIL_BASEDIR = 'thumbs'
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# For Aldryn blog
ALDRYN_BOILERPLATE_NAME='bootstrap3'

FILER_ENABLE_PERMISSIONS = True

# Ilmo
ILMO_EMAIL_CONFIGURED = True
ILMO_EMAIL_TEMPLATE_PATH = 'email'
ILMO_EMAIL_CONFIRMATION_FROM = 'noreply@satakuntatalo.fi'
