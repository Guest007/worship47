# STATIC
# ------------------------------------------------------------------------------
import os

from worship47.settings import BASE_DIR

FILES_BASE = os.getenv("FILES_BASE", "..")

STATIC_ROOT = BASE_DIR / "staticfiles/"
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static/",
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"
