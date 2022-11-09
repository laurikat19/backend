from rest_framework import serializers

from backend.clase.models import Clase

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "salon": instance.salon,
            "horario": instance.Horario,
            "profesor_id": instance.profesor.id,
            "profesor": instance.profesor.nombre,
            "asignatura_id": instance.asignatura.id,
            "asignatura": instance.asignatura.nombre,
        }