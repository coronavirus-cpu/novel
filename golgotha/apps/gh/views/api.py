from rest_framework import generics, permissions
from apps.gh.serializers import GHUserSerializer
from apps.gh.models import GitHubUser


class GHUserListAPIView(generics.ListCreateAPIView):
    serializer_class = GHUserSerializer
    queryset = GitHubUser.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
