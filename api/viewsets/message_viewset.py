from rest_framework import viewsets, mixins
from message.models.message_model import MessageModel
from ..serializers.message_serializer import MessageSerializer


class MessageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = MessageModel.objects.filter(status=True)
        topic_id = self.request.GET.get('topic_id')
        if topic_id is not None:
            queryset = queryset.filter(topic_id=topic_id)
        return queryset
    