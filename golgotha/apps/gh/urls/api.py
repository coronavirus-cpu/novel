from django.urls import path
from apps.gh.views.api import GHUserListAPIView

app_name = "gh"

urlpatterns = [path("", GHUserListAPIView.as_view(), name="index")]
