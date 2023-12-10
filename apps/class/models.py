from django.db import models

from utils import BaseModel


class Subject(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Class(BaseModel):
    title = models.CharField(max_length=255)
    subjects = models.ManyToManyField(Subject)
    students = models.ManyToManyField("student.Student")

    def __str__(self):
        return self.title
