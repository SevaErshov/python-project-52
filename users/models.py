from django.db import models


class UserCreated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
