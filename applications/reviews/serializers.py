from rest_framework import serializers
from applications.reviews.models import Review
from applications.rentals.choices.rental_status import RentStatus


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'room', 'rent', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate(self, attrs):
        user = self.context['request'].user

        # 1. Роль
        if user.role != 'GUEST':
            raise serializers.ValidationError("Лише користувач з роллю 'GUEST' може залишити відгук.")

        # 2. Один відгук на одну кімнату
        if Review.objects.filter(reviewer=user, room=attrs['room']).exists():
            raise serializers.ValidationError("Ви вже залишили відгук для цієї кімнати.")

        # 3. Перевірка оренди
        rent = attrs.get('rent')
        if rent.lessee != user:
            raise serializers.ValidationError("Ви можете залишити відгук лише до своєї оренди.")
        if rent.room != attrs['room']:
            raise serializers.ValidationError("Ця оренда не відповідає вибраній кімнаті.")
        if rent.status != RentStatus.COMPLETED.name:
            raise serializers.ValidationError("Відгук можна залишити лише після завершення оренди.")

        return attrs