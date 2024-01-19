from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializer import CustomUserSerializer
from .permission import AllowPOSTOnly  # Assuming AllowPOSTOnly is a custom permission class

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing CustomUser instances.

    Attributes:
        queryset: A queryset that includes all CustomUser instances.
        serializer_class: The serializer class for CustomUser instances.
        permission_classes: A list of permission classes; this viewset only allows POST requests.
        pagination_class: The pagination class for splitting the queryset into page-sized chunks.

    Methods:
        get_queryset: Custom method to retrieve a filtered queryset based on a 'q' query parameter,
                      or all CustomUser instances if no parameter is provided.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowPOSTOnly]
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        """
        Retrieves a queryset of CustomUser objects based on the given query.

        Parameters:
            self (object): The instance of the class.
        
        Returns:
            QuerySet: A queryset of CustomUser objects that match the given query.
        """
        query = self.request.GET.get('q')
        if query:
            return CustomUser.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query)
            )
        return CustomUser.objects.all()

class ListFriends(generics.ListAPIView):
    """
    A view for listing all friends of the currently authenticated user.

    Attributes:
        permission_classes: A list of permission classes; this view requires the user to be authenticated.
        serializer_class: The serializer class for CustomUser instances.
        pagination_class: The pagination class for splitting the queryset into page-sized chunks.

    Methods:
        get_queryset: Retrieves the queryset that represents the friends of the currently authenticated user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return self.request.user.friends.all()
