from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from backend.profesor.models import Profesor
from backend.profesor.api.serializers.serializer import ProfesorSerializer

class ProfesorViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = ProfesorSerializer
    queryset = Profesor.objects.filter(is_active=True)
    lookup_field = 'id'

    def perform_destroy(self, instance):
        """Disable profile."""
        instance.is_active = False
        instance.save()