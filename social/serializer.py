from rest_framework import serializers

from .models import FriendRequest


class FriendRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for FriendRequest model.
    
    This serializer provides a way to output all fields of the FriendRequest model
    while making 'status' and 'from_user' fields read-only.
    """
    
    class Meta:
        model = FriendRequest
        fields = '__all__'
        read_only_fields = ['status', 'from_user']
    

class ChangeRequestStatusSerializer(serializers.ModelSerializer):
    
    """
    Serializer for updating the status of a FriendRequest.
    
    This serializer is specifically for changing the 'status' field of a
    FriendRequest instance. It includes a ChoiceField for 'status' with options
    'accepted' or 'rejected'. The 'id' field is used to identify the specific
    FriendRequest to be updated.
    """
    
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    id = serializers.IntegerField()
    
    class Meta:
        model = FriendRequest
        fields = ['status', 'id']
    
    def create(self, validated_data):
    
        """
        Handles creating or updating a FriendRequest instance with the given
        validated data containing 'status' and 'id'.

        If the 'status' is 'accepted', adds the 'from_user' to the 'to_user's
        friends list; if 'rejected', removes the 'from_user' from the 'to_user's
        friends list.

        Returns:
            The updated FriendRequest instance.
        """
        
        status = validated_data['status']
        friend_request = FriendRequest.objects.get(pk=validated_data['id'])
        friend_request.status = status
        friend_request.save()
        if status=='accepted':
            friend_request.to_user.friends.add(friend_request.from_user)
        else:
            friend_request.to_user.friends.remove(friend_request.from_user)
        return friend_request

