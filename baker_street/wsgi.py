"""
WSGI config for baker_street project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
# Use local 'development' settings as the default
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baker_street.settings.local")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(get_wsgi_application())
