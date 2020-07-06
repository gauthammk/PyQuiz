from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer


# User Viewset for CRUD
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
