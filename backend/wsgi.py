"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# Importing necessary modules
import os

# Importing the get_wsgi_application function from django.core.wsgi
from django.core.wsgi import get_wsgi_application

# Setting the DJANGO_SETTINGS_MODULE environment variable to 'backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Getting the WSGI application for the backend project
application = get_wsgi_application()

