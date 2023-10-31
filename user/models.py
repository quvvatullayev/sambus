from django.db import models
from django.contrib.auth.models import User

class UserModel(User):
    location = models.JSONField()

    def __str__(self) -> str:
        return self.username