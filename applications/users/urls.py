from django.urls import path
from applications.users import views
from applications.users.views import UserRegistrationView

urlpatterns = [
    path("", views.UserListView.as_view(), name="user-list"),
    path("<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
    path('register/', UserRegistrationView.as_view(), name='user-register')
]