from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta

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
        if new_status not in ["CONFIRMED", "REJECTED"]:
            return Response({"detail": "Неправильний статус."}, status=status.HTTP_400_BAD_REQUEST)

        rent.status = new_status
        rent.save()
        return Response({"detail": "Статус успішно змінено."}, status=status.HTTP_200_OK)