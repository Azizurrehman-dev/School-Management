from rest_framework.viewsets import ModelViewSet

from .serializers import SubjectSerializer, Subject, ClassSerializer, Class


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
