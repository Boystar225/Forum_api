from rest_framework import serializers 
from message.models.message_model import MessageModel

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields=['topic', 'content']
        extra_kwargs = {
            'topic': {'label': 'Sujet'},
            'content': {'label': 'Contenus'},
        }