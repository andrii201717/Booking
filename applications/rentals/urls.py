from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.rentals.views import RentViewSet
from applications.rooms.views import RoomViewSet

router = DefaultRouter()
router.register('rents', RentViewSet, basename='rent')
router.register(r'rooms', RoomViewSet, basename='room')

urlpatterns = [
    path('', include(router.urls)),
]