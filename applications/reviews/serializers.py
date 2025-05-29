from rest_framework import serializers
from applications.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'room', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate(self, attrs):
        user = self.context['request'].user

        if user.role != 'GUEST':
            raise serializers.ValidationError("Лише користувач з роллю 'GUEST' може залишити відгук.")

        # Перевірка, чи вже існує відгук від цього користувача на цю кімнату
        if Review.objects.filter(reviewer=user, room=attrs['room']).exists():
            raise serializers.ValidationError("Ви вже залишили відгук для цього оголошення.")

        return attrs