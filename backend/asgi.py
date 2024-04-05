"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os  
# Importation du module os pour l'interaction avec le système d'exploitation

from django.core.asgi import get_asgi_application  
# Importation de la fonction get_asgi_application de Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  
# Configuration du module de paramètres Django

application = get_asgi_application()  
# Obtention de l'application ASGI pour le déploiement
