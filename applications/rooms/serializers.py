from rest_framework import serializers
from applications.rooms.models.room import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'deleted_at', 'is_deleted']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)
