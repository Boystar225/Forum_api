from rest_framework import viewsets
from message.models.message_model import MessageModel
from ..serializers.message_serializer import MessageSerializer
from rest_framework.exceptions import MethodNotAllowed


class MessageViewSet(viewsets.ModelViewSet):
    
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = MessageModel.objects.filter(status=True)
        topic_id = self.request.GET.get('topic_id')
        if topic_id is not None:
            queryset = queryset.filter(topic_id=topic_id)
        return queryset
    
    
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE",detail="Suppression non autorisée.")
    
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT", detail="Modification complète non autorisée.")
    
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH", detail="Modification partielle non autorisée.")
    