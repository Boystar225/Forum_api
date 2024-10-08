from rest_framework import serializers
from topic.models.topic_model import TopicModel


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields=['id','forum', 'title']
        extra_kwargs = {
            'title': {'label': 'Titre du sujet'},
        }