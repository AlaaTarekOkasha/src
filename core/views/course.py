from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from core.models import Courses
from core.serializers import (
    CourseSerializer, 
    TrainerSerializer,
    TestemonialSerializer
)


class CourseView(ListAPIView):
    queryset = Courses.objects.live()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']


class TrainerView(ListAPIView):  
    queryset = Courses.objects.live()
    serializer_class = TrainerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']


class TestemonialView(ListAPIView):
    queryset = Courses.objects.live()
    serializer_class = TestemonialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']