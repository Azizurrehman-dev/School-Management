from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.teacher.models import Teacher

User = get_user_model()


class UserTeacherSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('request'):
            if self.context.get('request').method in ["PUT", "PATCH"]:
                self.fields.pop("password")

    username = serializers.CharField(max_length=150)

    def validate_username(self, value):
        try:
            if self.context['request'].method in ['PUT', 'PATCH']:
                user_id = self.context['request'].parser_context['kwargs']['pk']
                instance = User.objects.filter(teacher_user=user_id).first()
                if instance.username == value:
                    return value
        except Exception:
            pass
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already registered.")
        return value

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password")

    def create(self, validated_data):
        try:
            password = make_password(validated_data.pop('password'))
            return User.objects.create(**validated_data, password=password)
        except serializers.ValidationError:
            raise


class TeacherSerializer(serializers.ModelSerializer):
    user = UserTeacherSerializer()

    class Meta:
        model = Teacher
        fields = ("id", "user", "classes")

    @transaction.atomic
    def create(self, validated_data):
        try:
            user_serializer = UserTeacherSerializer(data=validated_data.pop("user"))
            user_serializer.is_valid(raise_exception=True)
            teacher = Teacher(user=user_serializer.save())
            teacher.classes.set(validated_data.get("classes"))
            teacher.save()
            return teacher
        except (ValidationError, Exception) as error:
            raise error

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            serializer = UserTeacherSerializer(instance=instance.user, data=validated_data.pop('user'),
                                               context=self.context)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return super().update(instance, validated_data)
        except (ValidationError, Exception):
            raise
