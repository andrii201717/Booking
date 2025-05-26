from django.urls import path
from .views import RentListCreateView

urlpatterns = [
    path('', RentListCreateView.as_view(), name='rent-list-create'),
]