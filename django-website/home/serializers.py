from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'first_name', 'last_name', 'about']