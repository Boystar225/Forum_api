from rest_framework import viewsets
from topic.models.topic_model import TopicModel
from ..serializers.topic_serializer import TopicSerializer, TopicDetailSerializer
from rest_framework.exceptions import MethodNotAllowed

class TopicViewSet(viewsets.ModelViewSet):
    serializer_class= TopicSerializer
    detail_serializer_class = TopicDetailSerializer

    def get_queryset(self):
        queryset = TopicModel.objects.filter(status=True)
        forum_id = self.request.GET.get('forum_id')
        if forum_id is not None:
            queryset = queryset.filter(forum_id=forum_id)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE",detail="Suppression non autorisée.")
    
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT", detail="Modification complète non autorisée.")
    
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH", detail="Modification partielle non autorisée.")
    