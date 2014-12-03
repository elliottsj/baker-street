from .base import *

# Disable debug in production
DEBUG = False
CELERY_ALWAYS_EAGER = True