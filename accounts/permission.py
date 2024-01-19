from rest_framework.permissions import BasePermission

class AllowPOSTOnly(BasePermission):
    """
    Custom permission to only allow unauthenticated POST requests.
    """
    
    def has_permission(self, request, view):
        # Grant permission if it's a POST request or the user is authenticated
        return request.method == 'POST' or (request.user and request.user.is_authenticated)
