from django.db import models  
# Importe le module models de Django

class Utilisateur(models.Model):  # Définit un modèle Utilisateur héritant de models.Model
    name = models.CharField(max_length=100)  # Déclare un champ de type CharField pour le nom
    password = models.CharField(max_length=100)  # Déclare un champ de type CharField pour le mot de passe

    class Meta:  # Définit les métadonnées du modèle
        # Supprimer la ligne ordering si vous n'avez pas besoin de trier par le champ created
        ordering = ['name']  # Définit l'ordre de tri par le champ name

    

        
    
       