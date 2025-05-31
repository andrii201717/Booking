from rest_framework import serializers
from applications.rentals.models.rent import Rent
from applications.rooms.models.room import Room
from applications.users.models import User

class RentSerializer(serializers.ModelSerializer):
    lessee = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='GUESTE'))
    rent = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

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
        read_only_fields = ['status', 'created_at']