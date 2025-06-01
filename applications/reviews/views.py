from rest_framework import generics, permissions
from applications.reviews.models import Review
from applications.reviews.serializers import ReviewSerializer


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Review.objects.filter(room_id=room_id)