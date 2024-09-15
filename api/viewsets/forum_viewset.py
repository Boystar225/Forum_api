from ..serializers.forum_serializer import ForumSerializer, ForumDetailSerializer
from rest_framework import viewsets
from forum.models.forum_model import ForumModel
from rest_framework.exceptions import MethodNotAllowed


class ForumViewset(viewsets.ModelViewSet):
    serializer_class =ForumSerializer
    detail_serializer_class = ForumDetailSerializer
    queryset = ForumModel.objects.filter(status=True)

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
    