from ..serializers.forum_serializer import ForumSerializer
from ..serializers.forum_detail_serializer import ForumDetailSerializer
from rest_framework import viewsets
from forum.models.forum_model import ForumModel
from rest_framework.exceptions import MethodNotAllowed


class ForumViewset(viewsets.ModelViewSet):
    http_method_names = ['post', 'get']
    serializer_class = ForumSerializer
    detail_serializer_class = ForumDetailSerializer
    queryset = ForumModel.objects.filter(status=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
