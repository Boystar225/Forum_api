from rest_framework import serializers 
from message.models.message_model import MessageModel

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'