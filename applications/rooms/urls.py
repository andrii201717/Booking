from rest_framework.routers import DefaultRouter
from applications.rooms.views import RoomViewSet, AddressCreateView
from django.urls import path

router = DefaultRouter()
router.register('', RoomViewSet, basename='room')

urlpatterns = [
    path('addresses/', AddressCreateView.as_view(), name='address-create'),
    *router.urls
]