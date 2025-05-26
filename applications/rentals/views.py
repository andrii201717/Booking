from rest_framework import generics
from .models.rent import Rent
from .serializers import RentSerializer

class RentListCreateView(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
