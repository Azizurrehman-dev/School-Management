from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer, Student


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


