from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
