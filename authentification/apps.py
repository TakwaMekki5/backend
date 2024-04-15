from django.apps import AppConfig  
# Importe la classe AppConfig de Django

class AuthentificationConfig(AppConfig):  # Définit une classe AuthentificationConfig héritant de AppConfig
    default_auto_field = 'django.db.models.BigAutoField'  # Définit le champ par défaut pour les clés primaires automatiques
    name = 'authentification'  # Définit le nom de l'application




