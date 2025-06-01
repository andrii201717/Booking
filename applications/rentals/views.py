from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta

from applications.rentals.choices.rental_status import RentStatus
from applications.rentals.models.rent import Rent
from applications.rentals.serializers import RentSerializer


class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)

    @action(detail=True, methods=['post'], url_path='change-status')
    def change_status(self, request, pk=None):
        rent = self.get_object()
        user = request.user


        if rent.room.owner != user:
            return Response({"detail": "Ви не є власником цього житла."}, status=status.HTTP_403_FORBIDDEN)


        if timezone.now().date() > rent.start_date - timedelta(days=2):
            return Response({"detail": "Змінювати статус можна не пізніше ніж за 2 дні до початку оренди."},
                            status=status.HTTP_400_BAD_REQUEST)

        new_status = request.data.get("status")


        try:
            status_enum = RentStatus[new_status]
        except KeyError:
            return Response({"detail": f"Неправильний статус. Доступні: {[s.name for s in RentStatus]}"},
                            status=status.HTTP_400_BAD_REQUEST)

        rent.status = status_enum.name
        rent.save()

        return Response({"detail": f"Статус успішно змінено на «{rent.status}»."}, status=status.HTTP_200_OK)