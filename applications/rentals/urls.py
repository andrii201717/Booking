from rest_framework.routers import DefaultRouter
from applications.rentals.views import RentViewSet

router = DefaultRouter()
router.register('rents', RentViewSet, basename='rent')

urlpatterns = router.urls