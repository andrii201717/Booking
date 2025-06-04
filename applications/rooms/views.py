from rest_framework import viewsets, filters, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from applications.permissions.custom_permissions import IsOwnerOrReadOnly
from applications.rooms.models.room import Room
from applications.rooms.serializers import RoomSerializer, AddressSerializer
from applications.filters.room import RoomFilter
from applications.rooms.models.locations import Address

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # додаємо кастомний пермішен
    serializer_class = RoomSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = RoomFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at', 'sta']
    ordering = ['-created_at']


class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)