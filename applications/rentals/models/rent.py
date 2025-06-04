from datetime import timedelta

from django.utils import timezone
from django.db import models

from applications.rentals.choices.rental_status import RentStatus
from applications.rooms.models.room import Room
from applications.users.models import User


class Rent(models.Model):
    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rents',
        limit_choices_to={'role': 'GUEST'}
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='rents'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=RentStatus.choices(),
        default=RentStatus.PENDING.name
    )
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = 'rent'
        ordering = ['-created_at']
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_date__gt=models.F('start_date')),
                name='rent_valid_date_range'
            ),
            models.UniqueConstraint(
                fields=['guest', 'room', 'start_date', 'end_date'],
                name='unique_booking_per_user_rent_period'
            )
        ]

    def can_cancel(self):
        return (self.status == RentStatus.CONFIRMED.name and
                timezone.now().date() < self.start_date - timedelta(days=2))

    def __str__(self):
        return f'{self.guest} - {self.room}'