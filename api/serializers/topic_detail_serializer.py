from rest_framework import serializers
from topic.models.topic_model import TopicModel


class TopicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = "__all__"
