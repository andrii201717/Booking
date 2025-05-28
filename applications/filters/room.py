import django_filters
from applications.rooms.models.room import Room


class RoomFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    rooms_count_min = django_filters.NumberFilter(field_name="rooms_count", lookup_expr="gte")
    rooms_count_max = django_filters.NumberFilter(field_name="rooms_count", lookup_expr="lte")
    room_type = django_filters.CharFilter(field_name="room_type", lookup_expr="exact")
    city = django_filters.CharFilter(field_name="address__city", lookup_expr="icontains")

    class Meta:
        model = Room
        fields = []