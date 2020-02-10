from django_filters import rest_framework as filters
from .models import GitHubUser


class GHUserFilterSet(filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter(field_name="created_at")
    has_key = filters.BooleanFilter(field_name="has_key")

    class Meta:
        models = GitHubUser
        fields = ["has_key", "created_at"]
