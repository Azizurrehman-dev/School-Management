from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .viewsets import SubjectViewSet, ClassViewSet

router = DefaultRouter()

router.register("subjects", SubjectViewSet, basename="subject")
router.register("classes", ClassViewSet, basename="classes")

urlpatterns = [path("", include(router.urls))]
