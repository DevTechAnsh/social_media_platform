from django.urls import include, path
from rest_framework import routers

from .views import ChangeFriendRequestStatus, FriendRequestViewSet

router = routers.DefaultRouter()
router.register('request', FriendRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('status/<int:pk>/', ChangeFriendRequestStatus.as_view()),
]