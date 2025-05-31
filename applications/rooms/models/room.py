from django.db import models
from django.utils import timezone

from applications.rooms.choices.room_type import RoomType
from applications.rooms.managers.rooms import SoftDeleteManager
from applications.rooms.models.locations import Address
from applications.users.models.user import User


class Room(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='room'
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rooms_count = models.PositiveSmallIntegerField(default=0)
    room_type = models.CharField(max_length=36, choices=RoomType.choices())
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='room'
    )

    objects = SoftDeleteManager()

    def delete(self, *arg, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()

        self.save()

    class Meta:
        db_table = "room"
        constraints = [
            models.UniqueConstraint(fields=[
                'title',
                'address',
                'is_deleted'
            ],
                name='unique_listing_title_desc_address_not_deleted')
        ]

    def __str__(self):
        return self.title