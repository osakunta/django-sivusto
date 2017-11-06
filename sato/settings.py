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
if 'DJANGO_PRODUCTION' in os.environ:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    THUMBNAIL_DEBUG = False

    DATABASES = {
        'default': {
            'CONN_MAX_AGE': 0,
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': 'postgres',
            'NAME': 'django',
            'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
            'PORT': '',
            'USER': 'django'
        }
    }

    # Private filer files for Nginx
    FILER_SERVERS = {
        'private': {
            'main': {
                'ENGINE': 'filer.server.backends.nginx.NginxXAccelRedirectServer',
                'OPTIONS': {
                    'location': '/var/django/django-sivusto/smedia/filer_private',
                    'nginx_location': '/nginx_filer_private',
                },
            },
            'thumbnails': {
                'ENGINE': 'filer.server.backends.nginx.NginxXAccelRedirectServer',
                'OPTIONS': {
                    'location': '/var/django/django-sivusto/smedia/filer_thumbnails_private',
                    'nginx_location': '/nginx_filer_private_thumbnails',
                },
            },
        },
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'generic': {
                'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
                '()': 'logging.Formatter',
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'error_file': {
                'class': 'logging.FileHandler',
                'formatter': 'generic',
                'filename': '/var/log/gunicorn/error.log',
            },
            'access_file': {
                'class': 'logging.FileHandler',
                'formatter': 'generic',
                'filename': '/var/log/gunicorn/access.log',
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'gunicorn.error': {
                'level': 'INFO',
                'handlers': ['error_file'],
                'propagate': True,
            },
            'gunicorn.access': {
                'level': 'INFO',
                'handlers': ['access_file'],
                'propagate': False,
            },
        },
    }

else: # Development settings
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
    '.satakuntatalo.fi'
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
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',
                'aldryn_boilerplates.context_processors.boilerplate', # For Aldryn blog
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader', # For Aldryn blog
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
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'reversion',
    'sato',
    'image_gallery',
    'aldryn_bootstrap3',
	#'django-registration', #(Should not be in installed apps if using HMAC, leaving for reminder)

    # For Aldryn blog
    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_reversion',
    'parler',
    'sortedm2m',
    'taggit',

	# In-house-apps
	# 'ilmo_app',
]

LANGUAGES = (
    ('fi', gettext('fi')),
)

CMS_LANGUAGES = {
    1: [
        {
            'redirect_on_fallback': True,
            'code': 'fi',
            'hide_untranslated': False,
            'name': gettext('fi'),
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
    ('gallery_list.html', 'List galleries'),
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

CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}

MIGRATION_MODULES = {}

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format', 'Styles'],
    ],
    'skin': 'moono',
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
HALLITUSPALAUTE_SENDER = 'hallituspalaute@satakuntalalo.fi'
HALLITUSPALAUTE_RECIPIENTS = [
    'hallitus@satakuntatalo.fi',
]
