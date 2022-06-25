from django.urls import path, include
from rest_framework import routers
from common.views.userViews import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
]