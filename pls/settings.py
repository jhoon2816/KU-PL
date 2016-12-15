import os
from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ukb51_mr)ultwcb8ts*btk8exm)eng&_vs5ce*k_d18fko72wn'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # packages
    'django_summernote',

    # django apps
    'qna'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'pls.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pls.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ADMIN_MEDIA_URL = '/media/admin/'
ADMIN_MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Message tags with Bootstrap 3
MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': False,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    # 'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,

    # Set text direction : 'left to right' is default.
    'direction': 'ltr',

    # Change editor size
    'width': '100%',
    # 'height': '400',

    # Or, set editor language/locale forcely
    'lang': 'ko-KR',

    # prettifyHtml
    'prettifyHtml': True,

    # Customize toolbar buttons
    'toolbar': [
        # ['history', ['undo', 'redo']],
        ['highlight', ['highlight']],
        ['type', ['style']],
        ['style', ['bold', 'italic', 'underline', 'strikethrough', 'color']],
        ['paragraph', ['ul', 'ol']],
        ['insert', ['link', 'picture', 'video', 'table']],
        ['etc',['codeview', 'fullscreen', 'help']]
    ],

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,

    # You can add custom css/js for SummernoteWidget.
    'css': (),
    'js': (
        STATIC_URL + 'js/summernote-ext-highlight.js',
    ),

    # And also for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    'css_for_inplace': (),
    'js_for_inplace': (
        STATIC_URL + 'js/summernote-ext-highlight.js',
        # '//cdnjs.cloudflare.com/ajax/libs/codemirror/3.20.0/codemirror.css',
        # '//cdnjs.cloudflare.com/ajax/libs/codemirror/3.20.0/theme/monokai.css',
        # '//cdnjs.cloudflare.com/ajax/libs/codemirror/3.20.0/codemirror.js',
        # '//cdnjs.cloudflare.com/ajax/libs/codemirror/3.20.0/mode/xml/xml.js',
        # '//cdnjs.cloudflare.com/ajax/libs/codemirror/2.36.0/formatting.js',
    ),

    # You can disable file upload feature.
    'disable_upload': False,
}
