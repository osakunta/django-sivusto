# In production: SECRET_KEY, DATABASES and LOGGING are different
import os
gettext = lambda s: s
_ = lambda s: s

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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
        'default': {
            'CONN_MAX_AGE': 0,
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'kubernetes_django',
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'USER': os.getenv('POSTGRES_USER'),
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT', 5432)
        }
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

    # Email settings
    EMAIL_HOST = 'smtp-relay.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

    SERVER_EMAIL = 'django@satakuntatalo.fi'
    DEFAULT_FROM_EMAIL = 'noreply@satakuntatalo.fi'
    ADMINS = [('DjangoAdmin', os.getenv('DJANGO_ADMIN_EMAIL', 'localhost'))]

else:  # Development settings
    SECRET_KEY = 'verisecriit'
    DEBUG = True
    THUMBNAIL_DEBUG = True

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
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
]

# Application definition
ROOT_URLCONF = 'sato.urls'
WSGI_APPLICATION = 'sato.wsgi.application'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
# Used by django-registration to determine for how long accounts can be activated.
ACCOUNT_ACTIVATION_DAYS = 7

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
            os.path.join(BASE_DIR, 'hallituspalaute', 'templates'),
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
                'django.template.loaders.eggs.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',  # For Aldryn blog
            ],
        },
    },
]


MIDDLEWARE_CLASSES = [
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
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware'
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
    'sato',
    'aldryn_bootstrap3',
    # 'django-registration', #(Should not be in installed apps if using HMAC, leaving for reminder)

    # Raw HTML for quick fixes
    'cmsplugin_raw_html',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
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

CMS_STYLE_NAMES = (
    ('content-bg', _("content-bg")),
    ('container', _("container")),
    ('row', _("row")),
)

CMS_PERMISSION = False
CMS_PLACEHOLDER_CONF = {}

MIGRATION_MODULES = {}

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format', 'Styles'],
    ],
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

# Hallituspalaute
HALLITUSPALAUTE_SENDER = 'hallituspalaute@satakuntatalo.fi'
HALLITUSPALAUTE_RECIPIENTS = [
    'hallitus@satakuntatalo.fi',
]
