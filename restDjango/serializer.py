from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from restDjango.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age']
        # read_only_fields = ('id',)


