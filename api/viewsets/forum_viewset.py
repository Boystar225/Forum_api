from api.serializers.forum_serializer import ForumSerializer
from rest_framework import viewsets
from forum.models.forum_model import ForumModel
from rest_framework.exceptions import MethodNotAllowed


class ForumViewset(viewsets.ModelViewSet):
    serializer_class =ForumSerializer
    queryset = ForumModel.objects.all()
    
    #Surcharger la méthode pour empêcher le destroy 
    
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE",detail="Suppression non autorisée.")
    
     # Surcharge de la méthode update pour empêcher les modifications complètes
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT", detail="Modification complète non autorisée.")
    
    # Surcharge de la méthode partial_update pour empêcher les modifications partielles
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH", detail="Modification partielle non autorisée.")
    