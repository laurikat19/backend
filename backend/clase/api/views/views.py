from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from backend.clase.models import Clase
from backend.clase.api.serializers.serializer import ClaseSerializer

class ClaseViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = ClaseSerializer
    queryset = Clase.objects.filter(is_active=True)
    lookup_field = 'id'

    def perform_destroy(self, instance):
        """Disable profile."""
        instance.is_active = False
        instance.save()