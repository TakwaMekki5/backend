from django.urls import path  
# Importation de la fonction path depuis le module django.urls pour définir les chemins des URL
from authentification import views  
# Importation du module views depuis le package authentification pour importer les vues définies

urlpatterns = [  # Définition de la liste urlpatterns contenant les chemins des URL
    path('authentification/', views.Utilisateur_list),  # Définition du chemin d'URL '/authentification/' associé à la vue Utilisateur_list
    # Assurez-vous que le chemin de l'URL est correct
]

