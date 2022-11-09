from django.urls import include, path
from rest_framework.routers import DefaultRouter
from backend.profesor.api.views.views import ProfesorViewSet

router = DefaultRouter()
router.register(r'profesor', ProfesorViewSet, basename='profesor'),

urlpatterns = [
    path('', include(router.urls))
]
