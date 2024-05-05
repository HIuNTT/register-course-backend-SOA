from rest_framework import serializers

from .models import RegisterCourse


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterCourse
        fields = ['state']