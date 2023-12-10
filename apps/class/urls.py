from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import SubjectViewSet, ClassViewSet

router = DefaultRouter()

router.register("subjects", SubjectViewSet, basename="subject")
router.register("class", ClassViewSet, basename="class")

urlpatterns = [path("", include(router.urls))]
