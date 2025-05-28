
from rest_framework.views import APIView
from rest_framework.response import Response

class UserListView(APIView):
    def get(self, request):
        return Response({"message": "Список користувачів"})

class UserDetailView(APIView):
    def get(self, request, pk):
        return Response({"message": f"Деталі користувача з id {pk}"})