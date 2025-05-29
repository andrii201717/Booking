from django.urls import path
from applications.reviews.views import ReviewCreateView, ReviewListView

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='review-create'),
    path('room/<int:room_id>/', ReviewListView.as_view(), name='review-list'),
]