from rest_framework import serializers
from apps.gh.models import GitHubUser


class GHUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubUser
        exclude = ["id"]
