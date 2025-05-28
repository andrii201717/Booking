from django.urls import path, include

urlpatterns = [
    path('rooms/', include('applications.rooms.urls')),
    path('rents/', include('applications.rentals.urls')),

    path("users/", include("applications.users.urls"))
]