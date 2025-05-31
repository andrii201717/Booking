from rest_framework import serializers
from applications.rentals.models.rent import Rent
from applications.rooms.models.room import Room

class RentSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Rent
        fields = [
            'id',
            'guest',
            'room',
            'start_date',
            'end_date',
            'status',
            'created_at',
        ]
        read_only_fields = ['guest', 'status', 'created_at']