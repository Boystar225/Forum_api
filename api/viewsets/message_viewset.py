from rest_framework import viewsets
from message.models.message_model import MessageModel
from api.serializers.message_serializer import MessageSerializer
from rest_framework.exceptions import MethodNotAllowed


class MessageViewSet(viewsets.ModelViewSet):
    
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    
    #Surcharger la méthode pour empêcher le destroy 
    
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE",detail="Suppression non autorisée.")
    
     # Surcharge de la méthode update pour empêcher les modifications complètes
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT", detail="Modification complète non autorisée.")
    
    # Surcharge de la méthode partial_update pour empêcher les modifications partielles
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH", detail="Modification partielle non autorisée.")
    