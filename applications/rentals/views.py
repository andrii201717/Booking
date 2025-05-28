from rest_framework import viewsets, permissions
from applications.rentals.models.rent import Rent
from applications.rentals.serializers import RentSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(lessee=self.request.user)