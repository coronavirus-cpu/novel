from rest_framework import generics, permissions

from apps.gh.filters import GHUserFilterSet
from apps.gh.models import GitHubUser
from apps.gh.serializers import GHUserSerializer


class GHUserListAPIView(generics.ListCreateAPIView):
    serializer_class = GHUserSerializer
    queryset = GitHubUser.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = GHUserFilterSet
    ordering_fields = ["created_at"]
    search_fields = ["login", "email"]


class GHUserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = GHUserSerializer
    queryset = GitHubUser.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = "login"
    lookup_field = "login"
