from django.db import models
from django.utils import timezone


class GitHubUser(models.Model):
    login = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, default="unknown")
    followers = models.IntegerField(default=0)
    email = models.EmailField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    gh_url = models.URLField(max_length=255)
    has_key = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
