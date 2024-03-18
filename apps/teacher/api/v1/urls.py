from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .viewsets import TeacherViewSet

router = DefaultRouter()

router.register("teachers", TeacherViewSet, basename="subject")

urlpatterns = [path("", include(router.urls))]
