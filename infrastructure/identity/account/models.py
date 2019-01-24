from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    uuid = models.UUIDField(primary_key=True)
