from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination
from .models import FriendRequest
from .serializer import FriendRequestSerializer, ChangeRequestStatusSerializer
from .throttling import FriendRequestRateThrottle

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all().filter(status='pending')
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [FriendRequestRateThrottle]
    pagination_class = PageNumberPagination
    http_method_names = ['post', 'get']

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Friend request sent"}, status=status.HTTP_201_CREATED)

class ChangeFriendRequestStatus(APIView):
    serializer_class = ChangeRequestStatusSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        status = request.data.get('status')     
        serializer = self.serializer_class(data={'id': pk, 'status': status})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"message": f"Friend request {status}"})
