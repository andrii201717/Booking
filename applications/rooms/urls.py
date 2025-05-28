from rest_framework.routers import DefaultRouter
from applications.rooms.views import RoomViewSet

router = DefaultRouter()
router.register('', RoomViewSet, basename='room')

urlpatterns = router.urls