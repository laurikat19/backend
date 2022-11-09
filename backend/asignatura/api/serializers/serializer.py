from rest_framework import serializers

from backend.asignatura.models import Asignatura

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'