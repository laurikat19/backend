from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from backend.asignatura.models import Asignatura
from backend.asignatura.api.serializers.serializer import AsignaturaSerializer

class AsignaturaViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = AsignaturaSerializer
    queryset = Asignatura.objects.filter(is_active=True)
    lookup_field = 'nombre'

    def perform_destroy(self, instance):
        """Disable profile."""
        instance.is_active = False
        instance.save()