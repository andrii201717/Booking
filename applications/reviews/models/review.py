from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from applications.rentals.choices.rental_status import RentStatus
from applications.users.choices.roles import UserRoles


class Review(models.Model):
    reviewer = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews',
        limit_choices_to={'role': UserRoles.GUEST.name}
    )
    room = models.ForeignKey(
        'rooms.Room',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rent = models.ForeignKey(
        'rentals.Rent',
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        blank=True
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

    def clean(self):
        if self.reviewer.role != UserRoles.GUEST.name:
            raise ValidationError("Тільки користувач з роллю 'GUEST' може залишити відгук.")

        if self.rent.guest != self.reviewer:
            raise ValidationError("Відгук може залишити лише орендар цієї оренди.")

        if self.rent.status != RentStatus.COMPLETED.name:
            raise ValidationError("Відгук можна залишити лише після завершення оренди.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.reviewer} → {self.room}: {self.rating}'