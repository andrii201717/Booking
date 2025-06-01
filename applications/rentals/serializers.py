from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils import timezone

from applications.rentals.choices.rental_status import RentStatus
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

    def validate(self, attrs):
        guest = self.context["request"].user
        room = attrs["room"]
        start = attrs["start_date"]
        end = attrs["end_date"]


        if start < timezone.now().date():
            raise ValidationError("Неможливо створити оренду в минулому.")


        if Rent.objects.filter(
            guest=guest, room=room,
            start_date=start, end_date=end
        ).exists():
            raise ValidationError("Ви вже створили бронювання для цієї квартири на ці дати.")


        overlapping = Rent.objects.filter(
            guest=guest
        ).filter(
            Q(start_date__lte=end) & Q(end_date__gte=start)
        ).exclude(room=room)

        if overlapping.exists():
            raise ValidationError("У вас вже є бронювання іншої квартири, що перетинається з цими датами.")

        return attrs

    def update(self, instance, validated_data):
        new_status = validated_data.get("status")
        if new_status == RentStatus.COMPLETED.name:
            today = timezone.now().date()
            if today < instance.end_date:
                raise ValidationError("Неможливо завершити оренду до дати її завершення.")

        return super().update(instance, validated_data)