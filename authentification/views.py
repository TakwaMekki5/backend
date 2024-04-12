from rest_framework.response import Response  
# Importation de la classe Response de rest_framework pour gérer les réponses HTTP
from rest_framework.decorators import api_view  
# Importation du décorateur api_view de rest_framework pour définir une vue d'API
from rest_framework import status  
# Importation du module status de rest_framework pour gérer les codes de statut HTTP
from authentification.models import Utilisateur  
# Importation du modèle Utilisateur depuis le package authentification.models
from .serializers import UtilisateurSerializer  
# Importation du sérialiseur UtilisateurSerializer depuis le package courant
 
@api_view(['GET', 'POST'])  # Décorateur pour définir une vue d'API prenant en charge les méthodes GET et POST
def Utilisateur_list(request):
    if request.method == 'GET':  # Vérification si la méthode HTTP est GET
        snippets = Utilisateur.objects.all()  # Récupération de tous les objets Utilisateur depuis la base de données
        serializer = UtilisateurSerializer(snippets, many=True)  # Initialisation du sérialiseur avec les données récupérées
        return Response(serializer.data)  # Renvoi des données sérialisées dans la réponse HTTP
 
    elif request.method == 'POST':  # Vérification si la méthode HTTP est POST
        serializer = UtilisateurSerializer(data=request.data)  # Initialisation du sérialiseur avec les données de la requête
        if serializer.is_valid():  # Vérification de la validité des données sérialisées
            serializer.save()  # Sauvegarde des données dans la base de données
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Renvoi des données sérialisées avec le code de statut HTTP 201 (Créé)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Renvoi des erreurs de validation avec le code de statut HTTP 400 (Bad Request)