from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from common.serializers.userSerializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    用户管理的增删查改
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    用户组管理的增删查改
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer