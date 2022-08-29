import re
from turtle import pos
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializers import *
from .models import *

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CourseView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated, )    
    queryset = Courses.objects.live()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class ContentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated, )    
    serializer_class = ContentSerializer
    queryset = Courses.objects.live()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class EndContentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated, )    
    serializer_class = EndContentSerializer
    queryset = Courses.objects.live()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']   

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class CriteriaView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated, )    
    serializer_class = CriteriaSerializer
    queryset = Courses.objects.live()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class TrainerView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated, )    
    serializer_class = TrainerSerializer
    queryset = Courses.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class TestemonialView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated, )
    serializer_class = TestemonialSerializer
    queryset = Courses.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

def index(request):
    return render(request, 'index.html')