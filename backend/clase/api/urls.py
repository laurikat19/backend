# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from backend.clase.api.views.views import ClaseViewSet

router = DefaultRouter()
router.register(r'clase', ClaseViewSet, basename='clase'),


urlpatterns = [
    path('', include(router.urls))
]