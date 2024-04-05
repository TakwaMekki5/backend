from django.contrib import admin  
# Importe le module admin de Django
from .models import Utilisateur  
# Importe le modèle Utilisateur depuis le répertoire actuel

admin.site.register(Utilisateur)  # Enregistre le modèle Utilisateur auprès de l'interface d'administration de Django
# Register your models here.  # Commentaire précisant que les modèles sont enregistrés ici

