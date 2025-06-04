from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("auth/", include([
        path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    ])),
    path("users/", include("applications.users.urls")),
    path("reviews/", include("applications.reviews.urls")),
    path("rooms/", include("applications.rooms.urls")),
    path("rentals/", include("applications.rentals.urls")),
]