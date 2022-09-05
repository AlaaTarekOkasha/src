import re
from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics

from .serializers import *
from .models import *

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CourseView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):   
    queryset = Course.objects.live()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class ContentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): 
    queryset = Course.objects.live()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class EndContentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):   
    queryset = Course.objects.live()
    serializer_class = EndContentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']   

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class UserCriteriaView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): 
    queryset = Course.objects.live()
    serializer_class = UserCriteriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class TrainerView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):  
    queryset = Course.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

class TestemonialView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = TestemonialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ----------------------------------------------------------------------------------------------------------

def index(request):
    return render(request, 'index.html')