from rest_framework import serializers
from sujet.models.sujet_model import SujetModel


class SujetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SujetModel
        fields = '__all__'