from django.urls import path

from .viewsets import StudentListView

urlpatterns = [path("students/", StudentListView.as_view())]
