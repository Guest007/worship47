# Application definition

PRE_APPS = []

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
]

THIRD_PARTY_APPS = [
    "ckeditor",
    "tagulous",
    "versatileimagefield",
    "widget_tweaks",
    # 'extra_views',
    "rest_framework",
    "rest_framework.authtoken",
]

LOCAL_APPS = [
    "accounts.apps.AccountsConfig",
    "songs",  # .apps.SongsConfig',
]

INSTALLED_APPS = PRE_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
