"""
WSGI config for prospectpass project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

# from whitenoise.django import DjangoWhiteNoise



# application = DjangoWhiteNoise(application)

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prospectpass.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)