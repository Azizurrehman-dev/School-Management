from rest_framework.viewsets import ModelViewSet

from .serializers import TeacherSerializer, Teacher


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
