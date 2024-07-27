from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from restDjango.models import User
from .serializer import UserSerializer


class UserListCreateApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer