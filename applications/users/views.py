from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from applications.users.serializers import UserRegistrationSerializer
from applications.users.models import User

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserListView(APIView):
    def get(self, request):
        return Response({"message": "Список користувачів"})


class UserDetailView(APIView):
    def get(self, request, pk):
        return Response({"message": f"Деталі користувача з id {pk}"})