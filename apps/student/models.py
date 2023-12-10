from django.db import models

from utils import BaseModel


class Student(BaseModel):
    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Others", "Others")]
    roll_no = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}-{self.roll_no}'
