from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from applications.permissions.custom_permissions import IsOwnerOrReadOnly
from applications.rooms.models.room import Room
from applications.rooms.serializers import RoomSerializer
from applications.filters.room import RoomFilter


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
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']