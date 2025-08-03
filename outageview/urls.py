from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActiveOutageViewSet, ArchiveOutageList,ArchiveOutageNumber

router = DefaultRouter()
router.register(r'ActiveOutage', ActiveOutageViewSet, basename='activeoutage')
# If you're not using a viewset for Archive, no need to register it here

urlpatterns = [
    path('', include(router.urls)),  # This includes ViewSet-based routes

    # Function-based view with pagination
    path('archive-outages/', ArchiveOutageList, name='ArchiveOutageList'),
    path('archive-outages/<str:pk>/', ArchiveOutageNumber, name='ArchiveOutageNumber'),
]
