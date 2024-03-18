from rest_framework import serializers

from apps.student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "roll_no", "first_name", "last_name", "gender")
