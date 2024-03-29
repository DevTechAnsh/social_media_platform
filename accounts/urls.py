from django.urls import include, path
from rest_framework import routers
from .views import CustomUserViewSet, ListFriends

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('friends-list/', ListFriends.as_view()),
]
