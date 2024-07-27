from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import UserSerializer


class UserListCreateAPIView(APIView):
    def post(self, request):
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            user = serialized_data.save()
            return Response(data=serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data)
