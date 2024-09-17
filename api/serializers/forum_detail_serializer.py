from rest_framework import serializers
from forum.models.forum_model import ForumModel


class ForumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumModel
        fields="__all__"