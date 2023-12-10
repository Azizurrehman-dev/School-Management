from django.db import models

from utils.models import BaseModel


class Teacher(BaseModel):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, related_name="teacher_user")
    classes = models.ManyToManyField("class.Class")
