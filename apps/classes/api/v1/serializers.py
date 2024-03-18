from rest_framework import serializers

from apps.classes.models import Subject, Class


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "title")


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ("title", "subjects", "students")
