# STATIC
# ------------------------------------------------------------------------------
from worship47.settings import BASE_DIR

STATIC_ROOT = BASE_DIR.parent / 'static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.parent / 'staticfiles/',
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = BASE_DIR.parent / 'media/'
MEDIA_URL = '/media/'
