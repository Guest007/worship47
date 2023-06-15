import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / 'apps'
sys.path.append(os.path.join(BASE_DIR, 'apps'))

from .apps import INSTALLED_APPS  # NoQA
from .vars import *  # NoQA
from .middleware import *  # NoQA
from .templates import *  # NoQA
from .db import *  # NoQA
from .auth import *  # NoQA
from .admin import *  # NoQA
from .tagulous import *  # NoQA
from .localize import *  # NoQA
from .files import *  # NoQA
from .rest import *  # NoQA
from .logging import *  # NoQA

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

try:
    from local import * # NoQA
except:
    sys.stdout.write('No local settings\n')
