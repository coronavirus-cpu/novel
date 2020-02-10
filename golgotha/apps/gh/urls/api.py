from django.urls import path
from apps.gh.views.api import GHUserListAPIView, GHUserDetailAPIView

app_name = "gh"

urlpatterns = [
    path("", GHUserListAPIView.as_view(), name="index"),
    path("<str:login>/", GHUserDetailAPIView.as_view(), name="detail"),
]
