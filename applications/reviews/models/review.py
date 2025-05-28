from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from applications.users.choices.roles import UserRoles
from applications.users.models import User



class Review(models.Model):
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        limit_choices_to={'role': UserRoles.GUEST.name}
    )
    room = models.ForeignKey(
        'rooms.Room',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review'
        ordering = ['-created_at']
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                name='valid_rating_range'
            ),
            models.UniqueConstraint(
                fields=['reviewer', 'room'],
                name='one_review_per_room_per_user'
            )
        ]

    def save(self, *args, **kwargs):
        if self.reviewer.role != UserRoles.GUEST.name:
            raise ValidationError("Тільки користувач з роллю 'GUEST' може залишити відгук.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.reviewer} → {self.room}: {self.rating}'