from rest_framework import serializers  
# Importe le module serializers de rest_framework
from .models import Utilisateur  
# Importe le modèle Utilisateur du répertoire courant (package)

class UtilisateurSerializer(serializers.ModelSerializer):  # Définit un sérialiseur pour le modèle Utilisateur
    class Meta:  # Définit les métadonnées du sérialiseur
        model = Utilisateur  # Spécifie le modèle à sérialiser
        fields = '__all__'  # Inclut tous les champs du modèle dans la sérialisation

