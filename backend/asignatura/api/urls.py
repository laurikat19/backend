# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from backend.asignatura.api.views.views import AsignaturaViewSet

router = DefaultRouter()
router.register(r'asignatura', AsignaturaViewSet, basename='asignatura'),


urlpatterns = [
    path('', include(router.urls))
]