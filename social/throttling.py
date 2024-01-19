from rest_framework.throttling import UserRateThrottle


class FriendRequestRateThrottle(UserRateThrottle):
    rate = '3/min'