from rest_framework import serializers
from .models.rent import Rent

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'
