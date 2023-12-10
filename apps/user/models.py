from django.contrib.auth.models import AbstractUser
from django.db import models

from utils import BaseModel


class User(AbstractUser, BaseModel):
    is_admin = models.BooleanField(default=False)
