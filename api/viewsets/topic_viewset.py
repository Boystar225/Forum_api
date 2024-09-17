from rest_framework import viewsets
from topic.models.topic_model import TopicModel
from ..serializers.topic_serializer import TopicSerializer
from ..serializers.topic_detail_serializer import TopicDetailSerializer


class TopicViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', 'get']
    serializer_class = TopicSerializer
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
