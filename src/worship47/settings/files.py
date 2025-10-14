# STATIC
# ------------------------------------------------------------------------------
import os

from worship47.settings import BASE_DIR

FILES_BASE = os.getenv("FILES_BASE", "..")

STATIC_ROOT = f"{FILES_BASE}/staticfiles/"
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
MEDIA_ROOT = f"{FILES_BASE}/media/"
MEDIA_URL = "/media/"
