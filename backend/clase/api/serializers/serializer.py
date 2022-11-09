from rest_framework import serializers

from backend.clase.models import Clase

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'