import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / "apps"
sys.path.append(os.path.join(BASE_DIR, "apps"))

from .admin import *  # NoQA
from .apps import INSTALLED_APPS  # NoQA
from .auth import *  # NoQA
from .db import *  # NoQA
from .files import *  # NoQA
from .localize import *  # NoQA
from .logging import *  # NoQA
from .middleware import *  # NoQA
from .rest import *  # NoQA
from .tagulous import *  # NoQA
from .templates import *  # NoQA
from .vars import *  # NoQA


EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

if DEBUG:  # noqa: F405 (imported from .vars)
    try:
        from .local import *  # NoQA
    except ModuleNotFoundError:
        sys.stdout.write("No local settings\n")
    except Exception as e:  # noqa: BLE001
        sys.stdout.write(f"Failed with exception {repr(e)}")
