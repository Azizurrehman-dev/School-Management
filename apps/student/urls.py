from django.urls import path

from apps.student.views import StudentListView

urlpatterns = [path("students/", StudentListView.as_view())]
