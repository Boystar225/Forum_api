from rest_framework import serializers
from forum.models.forum_model import ForumModel


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumModel
        fields=['id','name', 'description']
        extra_kwargs = {
            'name': {'label': 'Nom du forum'}
        }