from rest_framework import generics, permissions
from applications.reviews.models import Review
from applications.reviews.serializers import ReviewSerializer

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Хоча тут queryset не обов'язковий, краще явно його задати:
        return Review.objects.all()

    def perform_create(self, serializer):
        # Додатково можна явно встановити користувача, але це не обов’язково,
        # оскільки в серіалізаторі є HiddenField(default=CurrentUserDefault())
        serializer.save(reviewer=self.request.user)

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Review.objects.filter(room_id=room_id)