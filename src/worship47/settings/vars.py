import os


SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = bool(os.getenv("DEBUG", default=0))
# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(" ")
ROOT_URLCONF = "worship47.urls"
WSGI_APPLICATION = "worship47.wsgi.application"
SITE_ID = 1
APPEND_SLASH = False
